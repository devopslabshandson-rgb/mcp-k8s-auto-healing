# Kubernetes Auto Scaling + Slack Alerts

## Setup

1. Start Minikube
2. Install Metrics Server
3. Deploy:
   kubectl apply -f k8s/

4. Run watcher:
   docker build -t watcher ./watcher
   docker run -e SLACK_WEBHOOK=your_webhook watcher

## Result
Pods auto-scale + Slack alerts
