from src.detector.cloudwatch import fetch_cloudwatch_events
from src.detector.rules import failed_login_rule
from src.detector.report import save_alerts

LOG_GROUP = "cloud-threat-detection"

logs = fetch_cloudwatch_events(LOG_GROUP)

alerts = failed_login_rule(logs, threshold=4, window_minutes=5)

for alert in alerts:
    print(alert)

save_alerts(alerts, "alerts.json")
print("Saved alerts to alerts.json")