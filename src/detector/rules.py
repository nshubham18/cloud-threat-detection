from datetime import timedelta

def failed_login_rule(events, threshold=4, window_minutes=5):
    alerts = []

    # sort events by time
    events = sorted(events, key=lambda x: x["ts"])

    # keep only FAIL login events
    fail_events = [e for e in events if e["event"] == "login" and e["result"] == "FAIL"]

    # group fail events by user
    users = {}
    for e in fail_events:
        users.setdefault(e["user"], []).append(e)

    window = timedelta(minutes=window_minutes)

    for user, fails in users.items():
        # sliding window check
        i = 0
        for j in range(len(fails)):
            while fails[j]["ts"] - fails[i]["ts"] > window:
                i += 1

            count_in_window = j - i + 1

            if count_in_window >= threshold:
                alerts.append(
                    f"ALERT: {user} had {count_in_window} failed logins within {window_minutes} minutes."
                )
                break

    return alerts