from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")

def home():
    return "arezooo khenge arezooo khenge"
@app route("/Bigkhengool")
def hi():
    return requests.get('https://instagram.com/arezoo.rajabloo')

if __name__ == "__main__":
    import os 
    PORT = os.getenv("PORT",5000)
    app.run("0.0.0.0",PORT)
