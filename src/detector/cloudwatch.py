import json
import boto3
from datetime import datetime, timezone

def fetch_cloudwatch_events(log_group: str, limit: int = 200):
    client = boto3.client("logs")

    resp = client.filter_log_events(
        logGroupName=log_group,
        limit=limit
    )

    events = []
    for e in resp.get("events", []):
        msg = e.get("message", "").strip()
        if not msg:
            continue

        obj = json.loads(msg)

        # same timestamp conversion you already use
        obj["ts"] = datetime.fromisoformat(obj["ts"].replace("Z", "+00:00")).astimezone(timezone.utc)

        events.append(obj)

    return events