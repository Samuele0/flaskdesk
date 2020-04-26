# flaskdesk
framework for developing desktop electron-like apps using flask and a webview.

##Usage


~~~Python
import flask
from flaskdesk.webview import FlaskDeskApp

app = flask.Flask(__name__)
fdapp = FlaskDeskApp(app)


@app.route("/")
def home():
    return "HELLO WORLD!"


if __name__ == "__main__":
    fdapp.run()
