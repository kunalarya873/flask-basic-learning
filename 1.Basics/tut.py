from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/index/")
def index():
    name = "kunal"
    return render_template("index.html", name = name)

app.run(debug=True)