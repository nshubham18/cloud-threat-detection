import json

def save_alerts(alerts, path="alerts.json"):
    with open(path, "w") as f:
        json.dump(alerts, f, indent=2)