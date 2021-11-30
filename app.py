from flask import Flask,render_template,request,flash


app = Flask(__name__)
app.secret_key = "mma_1997"
@app.route("/")

def home():
    return render_template('index.html')
    

@app.route("/greet",methods=["POST","GET"])
def greet():
    flash("HELLO " +str(request.form["name_input"]))
    return render_template('index.html')
    

