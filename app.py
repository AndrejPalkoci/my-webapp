from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from my Python web app!</h1><p>Deployed on Railway via PaaS.</p>"

@app.route("/movies")
def movies():
    return "<h1>Movies endpoint</h1><p>This would connect to MongoDB here.</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)