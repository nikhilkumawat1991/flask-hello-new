from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
def index():
    return "<h1>Hello Azure!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

