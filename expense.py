from flask import Flask, render_template

applicationName = Flask(__name__)

@applicationName.route("/")
def helloWorld(name=None):
    return render_template("test.html", name=name)


