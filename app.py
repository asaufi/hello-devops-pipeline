from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
visits = Counter("web_visits_total", "Total number of visits")

@app.route("/")
def home():
    visits.inc()
    return "👋 Hello from Flask + Docker + CI/CD!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
