__author__ = 'stamaimer'

from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template

import WaterSupplyMonitor

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():

    return render_template("addinformurl.html")


@app.route("/addinformurl", methods=["POST"])
def AddInformURL():

    url = request.form["url"]

    WaterSupplyMonitor.AddInfomURL.delay(url)

    return jsonify({"status": 0, "message": "success"}), 200


if __name__ == "__main__":

    app.run(host="104.236.129.194", port=9814, debug=True)

