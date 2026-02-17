import json
from datetime import datetime, timezone

def load_logs(path):
    events = []

    with open(path, "r") as f:
        for line in f:
            e = json.loads(line)

            # convert text timestamp -> real datetime object
            e["ts"] = datetime.fromisoformat(e["ts"].replace("Z", "+00:00")).astimezone(timezone.utc)

            events.append(e)

    return events