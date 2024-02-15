from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template('firstpage.html')


@app.route("/about")
def about():
    n1="Rakesh Gupta"
    return render_template('aboutus.html',name=n1)

app.run()