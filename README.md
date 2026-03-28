# Auto Scaling using Prometheus and Google Cloud Platform

## Overview
This project demonstrates an auto-scaling system where a **local virtual machine** monitors its CPU usage and automatically triggers deployment to a **cloud virtual machine (GCP)** when the load exceeds a defined threshold.

The system simulates real-world cloud scaling behavior using monitoring tools and a Python-based decision engine.

---

## Architecture

Local VM → Node Exporter → Prometheus → Auto-scale Script → GCP VM → Cloud Application

---

## ⚙️ Technologies Used

- **UTM** (Local Virtual Machine)
- **Ubuntu 22.04**
- **Prometheus** (Monitoring)
- **Node Exporter** (Metrics Collection)
- **Python** (Flask, Requests)
- **Google Cloud Platform (GCP)**

---

## How It Works

1. **Node Exporter** collects system metrics (CPU, memory, etc.)
2. **Prometheus** scrapes and processes these metrics
3. A Python script (`autoscale.py`) queries Prometheus
4. If CPU usage exceeds **75%**, a trigger is sent to the cloud VM
5. The cloud VM runs a Flask server (`cloud.py`)
6. Upon receiving the trigger, the application (`app.py`) is deployed

---

## 📁 Project Structure

auto-scaling-project/
│
├── local_vm/
│   ├── autoscale.py
│   ├── prometheus.yml
│   └── setup_commands.txt
│
├── cloud_vm/
│   ├── app.py
│   ├── cloud.py
│   └── requirements.txt
│
├── architecture.png
│
├── prometheus_graph.png
├── autoscale_output.png
├── cloud_output.png
└── final_output.png
│
└── README.md

---

## Setup Instructions

### Local VM Setup

# Start Node Exporter
./node_exporter

# Start Prometheus
./prometheus --config.file=prometheus.yml

# Run Auto-scaling script
python autoscale.py

---

Cloud VM Setup (GCP)

# Activate environment
source myenv/bin/activate

# Run cloud trigger server
sudo myenv/bin/python cloud.py


---

Simulate CPU Load

yes > /dev/null &


---

📊 Monitoring

Prometheus provides real-time monitoring and visualization of CPU usage.

Access Prometheus UI:

http://<LOCAL_VM_IP>:9090


---

🌐 Output

After scaling is triggered, the application is deployed on the cloud:

http://<GCP_EXTERNAL_IP>


---

## 📸 Screenshots

📈 Prometheus Graph

Shows CPU usage increasing over time.

⚙️ Auto-scale Script Output

Displays CPU values and scaling trigger.

☁️ Cloud Output

Shows cloud VM receiving trigger and starting application.

🌐 Final Application

Deployed UI confirming successful scaling.

---

## 🎥 Video Demonstration

https://drive.google.com/file/d/1sONK2N-pkg4GdB4gmKLq8WOriz-DKhfr/view?usp=sharing


---

## Key Features
-	Real-time monitoring using Prometheus
-	Threshold-based auto-scaling
-	Integration with Google Cloud Platform
-	Modular and scalable architecture

---

## Learning Outcomes
-	Understanding of monitoring systems
-	 Working with Prometheus and Node Exporter
-	 Cloud deployment using GCP
-	 Designing event-driven systems

---

Conclusion

This project demonstrates a complete pipeline from resource monitoring to automated cloud deployment, simulating real-world auto-scaling systems used in modern cloud infrastructures.

---


