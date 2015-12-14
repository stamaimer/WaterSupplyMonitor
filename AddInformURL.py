__author__ = 'stamaimer'

from flask import Flask
from flask import request
import WaterSupplyMonitor

app = Flask(__name__)

@app.route("/addinformurl", methods=["POST"])
def AddInformURL():

    url = request.form["url"]

    WaterSupplyMonitor.AddInfomURL(url)


if __name__ == "__main__":

    app.run(host="104.236.129.194", port=80, debug=True)

