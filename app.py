import streamlit as st
import time
from dataclasses import dataclass
from typing import Dict, Any, List, Optional

st.set_page_config(page_title="AI Incident Detection Agent", layout="wide")

st.title("🛡️ AI Incident Detection Agent")
st.markdown("Real-time telemetry monitoring, automated investigation, and triage.")

# --- Models & Mock Data ---
@dataclass
class RawEvent:
    event_id: str
    user_id: str
    ip_address: str
    action: str
    timestamp: float

class PerceptionFilter:
    def __init__(self, failure_threshold: int = 3, window_seconds: int = 60):
        self.failure_threshold = failure_threshold
        self.window_seconds = window_seconds
        self.history: List[RawEvent] = []

    def evaluate(self, event: RawEvent) -> Optional[Dict[str, Any]]:
        self.history.append(event)
        current = event.timestamp
        self.history = [e for e in self.history if current - e.timestamp <= self.window_seconds]
        
        failures = [e for e in self.history if e.ip_address == event.ip_address and e.action == "login_failed"]
        if len(failures) >= self.failure_threshold:
            return {
                "alert_type": "BRUTE_FORCE_SUSPECTED",
                "ip_address": event.ip_address,
                "target_account": event.user_id,
                "failure_count": len(failures),
            }
        return None

class DetectionAgent:
    IP_DB = {
        "203.0.113.42": {"score": 95, "tag": "Tor Exit Node / Scanner"},
        "192.168.1.10": {"score": 5, "tag": "Internal Range"},
    }

    def investigate(self, alert: Dict[str, Any]) -> Dict[str, Any]:
        ip = alert["ip_address"]
        rep = self.IP_DB.get(ip, {"score": 20, "tag": "Unknown"})
        is_high_risk = rep["score"] >= 80 and alert["target_account"] in ["root", "admin"]
        
        return {
            "verdict": "CRITICAL_ATTACK" if is_high_risk else "LOW_RISK_ANOMALY",
            "confidence": 0.98 if is_high_risk else 0.40,
            "ip": ip,
            "account": alert["target_account"],
            "reputation": rep["tag"],
            "threat_score": rep["score"],
            "rationale": f"Account '{alert['target_account']}' targeted from IP {ip} flagged as '{rep['tag']}'."
        }

# --- UI Controls ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Simulation Controls")
    threshold = st.slider("Failed Attempts Threshold", min_value=2, max_value=5, value=3)
    target_account = st.selectbox("Target Account", ["root", "alice", "admin"])
    source_ip = st.selectbox("Source IP", ["203.0.113.42", "192.168.1.10", "198.51.100.22"])
    trigger_btn = st.button("Simulate Attack Stream", type="primary")

with col2:
    st.subheader("Live Telemetry & Agent Output")
    if trigger_btn:
        detector = PerceptionFilter(failure_threshold=threshold)
        agent = DetectionAgent()
        
        st.info("Ingesting stream...")
        now = time.time()
        events = [
            RawEvent(f"evt_{i}", target_account, source_ip, "login_failed", now + i)
            for i in range(threshold)
        ]
        
        alert = None
        for ev in events:
            st.write(f"📥 `{ev.timestamp:.2f}` — User: **{ev.user_id}** | IP: `{ev.ip_address}` | Action: `{ev.action}`")
            alert = detector.evaluate(ev)

        if alert:
            st.warning("⚠️ Perception threshold breached. Agent investigating...")
            report = agent.investigate(alert)
            
            st.markdown("### 🧠 Agent Findings")
            res_col1, res_col2 = st.columns(2)
            res_col1.metric("Verdict", report["verdict"])
            res_col2.metric("Confidence", f"{report['confidence'] * 100:.0f}%")
            
            st.write(f"**Threat Details:** {report['reputation']} (Score: {report['threat_score']}/100)")
            st.write(f"**Rationale:** {report['rationale']}")
            
            if report["verdict"] == "CRITICAL_ATTACK":
                st.error(f"🛑 Automated Mitigation Applied: `iptables -A INPUT -s {report['ip']} -j DROP`")
            else:
                st.info("ℹ️ Low severity: Ticket dispatched to human reviewer.")