import flask
from flaskdesk.webview import FlaskDeskApp

app = flask.Flask(__name__)
fdapp = FlaskDeskApp(app)


@app.route("/")
def home():
    return "CIAO MONDO!"


if __name__ == "__main__":
    fdapp.run()
