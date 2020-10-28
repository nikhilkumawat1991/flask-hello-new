import logging
import json
import traceback
from flask import Flask, request, render_template,jsonify, redirect, url_for
import os
import yaml

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/services', methods=['GET','POST'])
def services():
    logging.debug("Redirecting to Device Connect Page")
    return render_template("services.html")    


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
