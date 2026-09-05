import os
import time
from dataclasses import dataclass
from typing import Any, Dict, List

import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Incident Detection Agent", page_icon="🛡️", layout="wide")


# =====================================================================
# 1. LOAD ML MODEL (IN-MEMORY FALLBACK - NO SUBPROCESS)
# =====================================================================
@st.cache_resource
def load_detection_model():
    model_path = "detector_model.pkl"
    if not os.path.exists(model_path):
        with st.spinner("Training baseline model from dataset for the first time..."):
            from train import train_and_export_model
            return train_and_export_model(model_path)
    return joblib.load(model_path)


model_artifact = load_detection_model()
ml_model = model_artifact["model"]
feature_cols = model_artifact["feature_cols"]


# =====================================================================
# 2. DATA STRUCTURES & THREAT INTELLIGENCE
# =====================================================================
@dataclass
class NetworkEvent:
    event_id: str
    src_ip: str
    account: str
    failed_attempts: int
    session_duration_sec: float
    bytes_sent_kb: float
    port_number: int
    timestamp: float

    def to_feature_vector(self) -> np.ndarray:
        return np.array([[
            self.failed_attempts,
            self.session_duration_sec,
            self.bytes_sent_kb,
            self.port_number
        ]])


class ThreatIntelligenceContext:
    KNOWN_IP_INTEL = {
        "198.51.100.22": {"threat_score": 92, "category": "Known Tor Exit Node / Scanner"},
        "203.0.113.45": {"threat_score": 88, "category": "Reported Botnet IP (AbuseIPDB)"},
        "192.168.1.50": {"threat_score": 2, "category": "Internal Corporate Range"},
        "10.0.0.12": {"threat_score": 0, "category": "Internal Gateway"},
    }

    PRIVILEGED_ACCOUNTS = {"root", "admin", "db_master", "security_admin"}

    @classmethod
    def lookup_ip(cls, ip: str) -> Dict[str, Any]:
        return cls.KNOWN_IP_INTEL.get(ip, {"threat_score": 15, "category": "Unindexed External IP"})

    @classmethod
    def is_privileged_account(cls, account: str) -> bool:
        return account.lower() in cls.PRIVILEGED_ACCOUNTS


# =====================================================================
# 3. DETECTION AGENT
# =====================================================================
class RemediationAgent:
    def __init__(self, context: type[ThreatIntelligenceContext]):
        self.context = context

    def investigate_incident(self, event: NetworkEvent, anomaly_score: float) -> Dict[str, Any]:
        ip_intel = self.context.lookup_ip(event.src_ip)
        is_privileged = self.context.is_privileged_account(event.account)

        ml_severity = min(1.0, max(0.0, (0.2 - anomaly_score) * 2.5))
        intel_severity = ip_intel["threat_score"] / 100.0

        risk_score = (0.5 * ml_severity) + (0.5 * intel_severity)
        if is_privileged:
            risk_score = min(1.0, risk_score + 0.20)

        if risk_score >= 0.75:
            verdict = "CRITICAL_ATTACK"
            action = f"APPLY FIREWALL BLOCK (iptables -A INPUT -s {event.src_ip} -j DROP)"
            action_type = "automated_block"
        elif risk_score >= 0.45:
            verdict = "SUSPICIOUS_ANOMALY"
            action = "TRIGGER HUMAN REVIEW TICKET (Escalated to SecOps Slack)"
            action_type = "quarantine"
        else:
            verdict = "BENIGN_NOISE"
            action = "LOG AND CONTINUE MONITORING"
            action_type = "allow"

        return {
            "verdict": verdict,
            "risk_score": round(risk_score * 100, 1),
            "ml_anomaly_score": round(float(anomaly_score), 4),
            "ip": event.src_ip,
            "account": event.account,
            "ip_category": ip_intel["category"],
            "is_privileged": is_privileged,
            "action": action,
            "action_type": action_type,
            "rationale": (
                f"Perception ML flagged feature vector on port {event.port_number}. "
                f"Originating IP {event.src_ip} classified as '{ip_intel['category']}'. "
                f"Target account '{event.account}' has privileged status: {is_privileged}."
            ),
        }


# =====================================================================
# 4. STREAMLIT UI
# =====================================================================
st.title("🛡️ AI Incident Detection & Autonomous Triage Agent")
st.markdown(
    "Architecture: **Dataset-Trained Isolation Forest (Perception)** $\\rightarrow$ "
    "**Reasoning Agent (Contextual Correlator)** $\\rightarrow$ "
    "**Automated Mitigation Engine**"
)

st.sidebar.header("🕹️ Simulation Engine")
mode = st.sidebar.radio("Select Input Mode", ["Batch Attack Simulation", "Manual Event Injection"])

agent = RemediationAgent(context=ThreatIntelligenceContext)

if mode == "Batch Attack Simulation":
    st.subheader("Automated Traffic Stream Evaluation")
    st.caption("Streams a batch of standard network sessions mixed with targeted anomalous events.")

    if st.button("Run Stream Ingestion", type="primary"):
        now = time.time()
        test_stream = [
            NetworkEvent("EVT-101", "192.168.1.50", "alice", 0, 150.0, 120.0, 443, now - 20),
            NetworkEvent("EVT-102", "10.0.0.12", "bob", 1, 30.0, 45.0, 80, now - 15),
            NetworkEvent("EVT-103", "198.51.100.22", "root", 18, 2.5, 3500.0, 22, now - 10),
            NetworkEvent("EVT-104", "192.168.1.50", "alice", 0, 400.0, 250.0, 443, now - 5),
            NetworkEvent("EVT-105", "203.0.113.45", "db_master", 3, 5.0, 8900.0, 4444, now - 1),
        ]

        for event in test_stream:
            features = event.to_feature_vector()
            pred = ml_model.predict(features)[0]
            score = ml_model.decision_function(features)[0]

            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"**Event ID:** `{event.event_id}`")
                st.write(f"IP: `{event.src_ip}` | Port: `{event.port_number}` | User: `{event.account}`")
                st.write(f"Payload: `{event.bytes_sent_kb} KB` | Failed Logins: `{event.failed_attempts}`")

            with col2:
                if pred == -1:
                    st.error(f"⚠️ **Tier 1 (ML Perception) Triggered**: Anomaly detected! (Score: {score:.3f})")
                    with st.spinner("Agent investigating context and querying threat databases..."):
                        report = agent.investigate_incident(event, score)

                    st.markdown(f"**Agent Verdict:** `{report['verdict']}` | **Risk Score:** `{report['risk_score']}%`")
                    st.write(f"💡 *Rationale:* {report['rationale']}")

                    if report["action_type"] == "automated_block":
                        st.error(f"🛑 **Action Executed:** `{report['action']}`")
                    else:
                        st.warning(f"🔔 **Action Executed:** `{report['action']}`")
                else:
                    st.success(f"✅ **Tier 1 (ML Perception)**: Benign Traffic (Score: {score:.3f}) — No agent intervention required.")

            st.divider()

else:
    st.subheader("Manual Event Parametric Test")
    st.caption("Craft an individual network packet event to test edge-case agent behavior.")

    c1, c2 = st.columns(2)
    with c1:
        in_ip = st.selectbox("Source IP Address", ["198.51.100.22", "203.0.113.45", "192.168.1.50", "142.250.180.46"])
        in_user = st.selectbox("Target Account", ["root", "admin", "db_master", "analyst_1", "guest"])
        in_port = st.number_input("Port Number", min_value=1, max_value=65535, value=22)

    with c2:
        in_failed = st.slider("Failed Logins in Window", min_value=0, max_value=50, value=12)
        in_duration = st.slider("Session Duration (seconds)", min_value=0.1, max_value=600.0, value=3.2)
        in_bytes = st.number_input("Payload Exfiltrated / Sent (KB)", min_value=0.0, max_value=100000.0, value=4500.0)

    if st.button("Evaluate Single Event", type="primary"):
        manual_event = NetworkEvent(
            event_id="MANUAL-TEST",
            src_ip=in_ip,
            account=in_user,
            failed_attempts=in_failed,
            session_duration_sec=in_duration,
            bytes_sent_kb=in_bytes,
            port_number=in_port,
            timestamp=time.time(),
        )

        features = manual_event.to_feature_vector()
        pred = ml_model.predict(features)[0]
        score = ml_model.decision_function(features)[0]

        st.markdown("### Evaluation Results")
        r_col1, r_col2 = st.columns(2)

        with r_col1:
            st.metric("Tier 1 Perception Status", "ANOMALY FLAGGED" if pred == -1 else "BENIGN")
            st.metric("Raw Model Decision Score", f"{score:.4f}")

        with r_col2:
            if pred == -1:
                report = agent.investigate_incident(manual_event, score)
                st.metric("Final Risk Severity", f"{report['risk_score']}%")
                st.metric("Agent Action Verdict", report["verdict"])
                st.info(f"**Rationale:** {report['rationale']}")
                st.code(report["action"], language="bash")
            else:
                st.success("The event falls well within the normal parameters of standard traffic. Dropped silently.")
