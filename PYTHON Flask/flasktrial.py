
# install python > 3.7

# install flask  - pip install flask

from flask import Flask

 

app = Flask(__name__)

 

@app.route("/")

def hello():

    return "Welcome to Python Flask"



@app.route("/hi")
def gm():
    return "Good Morning We are learning Flask"


app.run()

 