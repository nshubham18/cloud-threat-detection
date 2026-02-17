import json
import time
from pathlib import Path

LOG_GROUP = "cloud-threat-detection"
LOG_STREAM = "auth-events"

# your sample events (message stays the same)
messages = [
    {"ts":"2026-02-16T13:01:00Z","event":"login","user":"alice","result":"FAIL","ip":"10.0.0.5","city":"Dallas"},
    {"ts":"2026-02-16T13:01:10Z","event":"login","user":"alice","result":"FAIL","ip":"10.0.0.5","city":"Dallas"},
    {"ts":"2026-02-16T13:01:20Z","event":"login","user":"alice","result":"FAIL","ip":"10.0.0.5","city":"Dallas"},
    {"ts":"2026-02-16T13:01:30Z","event":"login","user":"alice","result":"FAIL","ip":"10.0.0.5","city":"Dallas"},
    {"ts":"2026-02-16T13:01:40Z","event":"login","user":"alice","result":"SUCCESS","ip":"10.0.0.5","city":"Dallas"},
]

# base timestamp = NOW in milliseconds
base_ms = int(time.time() * 1000)

payload = {
    "logGroupName": LOG_GROUP,
    "logStreamName": LOG_STREAM,
    "logEvents": []
}

# make them 1 second apart, starting from "now"
for i, msg in enumerate(messages):
    payload["logEvents"].append({
        "timestamp": base_ms + i * 1000,
        "message": json.dumps(msg)
    })

Path("data").mkdir(exist_ok=True)
with open("data/cloudwatch_events.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2)

print("Wrote data/cloudwatch_events.json with current timestamps")