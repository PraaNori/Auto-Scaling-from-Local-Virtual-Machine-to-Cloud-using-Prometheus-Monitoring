import requests
import time

# Prometheus API endpoint
PROM_URL = "http://localhost:9090/api/v1/query"

# CPU usage query
QUERY = '100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)'

# Threshold
THRESHOLD = 75

# GCP trigger URL (CHANGE THIS)
GCP_URL = "http://<YOUR_GCP_IP>/trigger"

# To avoid multiple triggers
triggered = False

print("🚀 Auto-scaling monitor started...\n")

while True:
    try:
        # Query Prometheus
        response = requests.get(PROM_URL, params={'query': QUERY})
        data = response.json()

        # Check if data exists
        if not data['data']['result']:
            print("No data received from Prometheus")
            time.sleep(3)
            continue

        # Extract CPU value
        cpu_usage = float(data['data']['result'][0]['value'][1])

        print(f"CPU Usage: {cpu_usage:.2f}%")

        # Trigger scaling
        if cpu_usage > THRESHOLD and not triggered:
            print("CPU HIGH → Triggering Cloud...")

            try:
                r = requests.post(GCP_URL)
                print(f"☁️ Cloud Response: {r.text}")
                triggered = True
            except Exception as e:
                print("Failed to trigger cloud:", e)

        # Reset trigger if CPU goes low
        if cpu_usage < 50:
            triggered = False

    except Exception as e:
        print("Error:", e)

    time.sleep(3)
