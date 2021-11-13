from flask import Flask, render_template, request
import requests
import random
import math
from random import seed
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # the app.route decorates the function so it says when this route is used go through this function
def index():
    num = random.random() * 1000000
    num2 = str(math.floor(num))
    print(type(num2))
    print(num2)
    return render_template("index.html", random=num2)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    return render_template("calculator.html")

@app.route('/probability', methods=['GET', 'POST'])
def probability():
    return render_template("probability.html")

if __name__ == "__main__":
    app.run(debug=True)