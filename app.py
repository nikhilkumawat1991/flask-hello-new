"""
Veea CONFIDENTIAL © 2020
All rights reserved NOTICE: All information contained herein is, and remains
the property of Veea and its suppliers, if any. The intellectual and technical
concepts contained herein are proprietary to Veea, and its suppliers  and may
be covered by U.S. and Foreign Patents, patents in process, and are protected by
trade secret or copyright law. Dissemination of this information or reproduction
of this material is strictly forbidden unless prior written permission is obtained
from Veea.
"""
###########################################################################
#LORAWAN CONFIGURATION MANAGER
###########################################################################

import logging
import json
import traceback
from flask import Flask, request, render_template,jsonify, redirect, url_for
from flask_cors import CORS, cross_origin
import os
import yaml

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/services', methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def services():
    logging.debug("Redirecting to Device Connect Page")
    return render_template("services.html")    


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
