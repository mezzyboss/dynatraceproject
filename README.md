# Dynatrace Trading Simulator – Full‑Stack Observability Demo

A containerized Python trading engine simulation with **Dynatrace OneAgent** integration, built to showcase **SRE‑grade observability** skills including custom metrics, anomaly detection, root‑cause analysis, and (optional) automated remediation.

---

## 🎯 Project Goals
- Demonstrate **end‑to‑end monitoring** of a distributed application using Dynatrace.
- Simulate **real‑time trading workloads** and failure scenarios.
- Show **actionable dashboards** and **AI‑driven incident analysis**.
- Integrate with **CI/CD pipelines** for deployment performance tracking.

---

## 🏗️ Architecture Overview

```
[ Python Trading Engine ]
          |
          v
[ Docker Container(s) ] --- [ Dynatrace OneAgent ]
          |
          v
[ Dynatrace SaaS Dashboard ]
          |
          +--> Davis AI Root Cause Analysis
          |
          +--> Optional Webhooks for Auto‑Remediation
```

---

## 🛠️ Tech Stack
- **Language**: Python 3.x (FastAPI or Flask)
- **Containerization**: Docker + Docker Compose
- **Monitoring**: Dynatrace SaaS (free trial)
- **CI/CD**: GitHub Actions
- **Logging**: Python `logging` module → Dynatrace ingestion

---

## 📦 Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/dynatrace-trading-sim.git
cd dynatrace-trading-sim
```

### 2️⃣ Install Dynatrace OneAgent (Local)
- Sign up for a **Dynatrace SaaS trial** at [dynatrace.com](https://www.dynatrace.com/trial/)
- Follow the setup wizard to get your **OneAgent install command**.
- Run that command **inside the Docker container** or on your local host.

### 3️⃣ Build and Run the App
```bash
docker-compose up --build
```

This starts the trading simulator and connects it to Dynatrace.

---

## 📊 Features to Test

- **Custom Metrics**: Latency, order throughput, error rates.
- **Fault Injection**: Trigger random delays or failures (`utils.py`).
- **Anomaly Detection**: Watch Davis AI flag unusual performance.
- **Root Cause Analysis**: Dynatrace pinpoints bottlenecks.
- **(Optional) Auto‑Remediation**: Trigger container restart via webhook.

---

## 🖥️ Dashboards & Outputs

📸 Add screenshots here of:
1. Service flow and dependency map.
2. Custom metrics panel.
3. Root cause analysis report.

---

## 🚀 CI/CD Integration
GitHub Actions pipeline will:
1. Build the Docker image.
2. Run tests.
3. Deploy/update the container.
4. Notify Dynatrace of new deployment for impact analysis.

---

## 📚 Learning Outcomes
By completing this project, you’ll be able to:
- Instrument Python apps for observability.
- Build Dynatrace dashboards for business‑critical metrics.
- Diagnose and respond to incidents with AI assistance.
- Demonstrate SRE‑ready skills to recruiters.

---

## 📄 License
MIT License — feel free to fork and adapt.

---

## 🙋 Author
Built by **Clinton** — Pragmatic mentor, SRE aspirant, and hands‑on cloud monitoring enthusiast.
```
