import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest


def generate_synthetic_network_dataset(num_samples: int = 5000) -> pd.DataFrame:
    """Generates synthetic network authentication & traffic flow data.

    Features:
      - failed_attempts: failed login count within 60 seconds
      - session_duration_sec: duration of active connection
      - bytes_sent_kb: outbound payload volume
      - port_number: destination port (22=SSH, 80=HTTP, 443=HTTPS, 8080=Alt)
    """
    np.random.seed(42)

    # 98% Normal traffic patterns
    num_normal = int(num_samples * 0.98)
    normal_failed = np.random.poisson(lam=0.2, size=num_normal)
    normal_duration = np.random.exponential(scale=120, size=num_normal) + 5
    normal_bytes = np.random.normal(loc=150, scale=40, size=num_normal).clip(10, 1000)
    normal_ports = np.random.choice([80, 443, 8080], size=num_normal, p=[0.4, 0.55, 0.05])

    normal_df = pd.DataFrame(
        {
            "failed_attempts": normal_failed,
            "session_duration_sec": normal_duration,
            "bytes_sent_kb": normal_bytes,
            "port_number": normal_ports,
            "is_anomaly": 0,
        }
    )

    # 2% Malicious / Anomalous traffic
    num_anom = num_samples - num_normal
    anom_failed = np.random.randint(5, 30, size=num_anom)
    anom_duration = np.random.exponential(scale=10, size=num_anom) + 0.5
    anom_bytes = np.random.exponential(scale=2000, size=num_anom) + 500
    anom_ports = np.random.choice([22, 23, 3389, 4444], size=num_anom)

    anom_df = pd.DataFrame(
        {
            "failed_attempts": anom_failed,
            "session_duration_sec": anom_duration,
            "bytes_sent_kb": anom_bytes,
            "port_number": anom_ports,
            "is_anomaly": 1,
        }
    )

    df = pd.concat([normal_df, anom_df], ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)
    return df


def train_and_export_model(model_filename: str = "detector_model.pkl"):
    """Trains the Isolation Forest model and saves it as a dictionary artifact."""
    df = generate_synthetic_network_dataset(num_samples=6000)
    feature_cols = ["failed_attempts", "session_duration_sec", "bytes_sent_kb", "port_number"]
    X = df[feature_cols]

    model = IsolationForest(
        n_estimators=100,
        contamination=0.02,
        random_state=42,
        n_jobs=-1,
    )
    model.fit(X)

    model_artifact = {
        "model": model,
        "feature_cols": feature_cols,
    }
    joblib.dump(model_artifact, model_filename)
    return model_artifact


if __name__ == "__main__":
    train_and_export_model()
    print("Model trained and saved to detector_model.pkl")
