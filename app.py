import logging
import json
from flask import Flask, request, render_template,jsonify, redirect, url_for
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/services', methods=['GET','POST'])
def services():
    return render_template("services.html")    


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
