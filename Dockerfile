FROM python:3.11-slim
WORKDIR /app
RUN apt update && apt install -y curl
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "watcher.py"]
