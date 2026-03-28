from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Auto Scaling Demo</title>
        <style>
            body {
                background: linear-gradient(135deg, #4facfe, #00f2fe);
                font-family: Arial, sans-serif;
                text-align: center;
                color: white;
                margin: 0;
                padding: 0;
            }
            .container {
                margin-top: 15%;
            }
            h1 {
                font-size: 60px;
                margin-bottom: 20px;
            }
            p {
                font-size: 24px;
            }
            .box {
                background: rgba(255, 255, 255, 0.2);
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.2);
            }
            .status {
                font-size: 28px;
                margin-top: 15px;
                color: #ffeb3b;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="box">
                <h1>Auto Scaling Successful</h1>
                <p>Your application is now running on the cloud!</p>
                <div class="status">☁️ Deployed on GCP VM</div>
            </div>
        </div>
    </body>
    </html>
    """

app.run(host='0.0.0.0', port=80)
