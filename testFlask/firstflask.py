from flask import Flask

rakesh=Flask(__name__)

@rakesh.route("/")
def hello():
    return "My First Project by Rakesh"


rakesh.run()