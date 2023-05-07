from flask import Flask

app = Flask(__baiust_cp_rank__)

@app.route("/")
def hello():
    return "Hello, World!"
