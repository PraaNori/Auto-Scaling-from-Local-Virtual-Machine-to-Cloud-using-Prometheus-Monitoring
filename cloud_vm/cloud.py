from flask import Flask
import os

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger():
    print("Scaling Trigger Received!")

    # Start app in background
    os.system("nohup python3 app.py &")

    return "Scaling Done", 200

app.run(host='0.0.0.0', port=80)
