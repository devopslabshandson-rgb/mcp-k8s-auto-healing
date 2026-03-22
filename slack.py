import requests
import os

def send_slack(message):
    webhook = os.getenv("SLACK_WEBHOOK")

    if not webhook:
        print("Slack webhook missing")
        return

    try:
        res = requests.post(webhook, json={"text": message})
        print("Slack sent:", res.status_code)
    except Exception as e:
        print("Slack error:", e)
