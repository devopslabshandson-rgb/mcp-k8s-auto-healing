import subprocess
import time
from slack import send_slack

last_replicas = 1

def get_replicas():
    try:
        output = subprocess.check_output(
            "kubectl get deploy my-app -o jsonpath='{.status.replicas}'",
            shell=True
        ).decode().replace("'", "").strip()

        return int(output) if output else 1
    except:
        return 1

while True:
    current = get_replicas()
    print("Replicas:", current)

    if current > last_replicas:
        send_slack(f"🚀 Scaled UP: {last_replicas} → {current}")
    elif current < last_replicas:
        send_slack(f"📉 Scaled DOWN: {last_replicas} → {current}")

    last_replicas = current
    time.sleep(10)
