from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")

def home():
    return render_template('index.html')
    



if __name__ == "__main__":
    import os 
    PORT = os.getenv("PORT",5000)
    app.run("0.0.0.0",PORT)
    
