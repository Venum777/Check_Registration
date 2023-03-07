import flask


app: flask.app.Flask = flask.Flask(__name__)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )