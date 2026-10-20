from flask import Flask

from routes import bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)