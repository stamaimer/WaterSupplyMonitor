__author__ = 'stamaimer'

from flask import Flask
from flask import request
import WaterSupplyMonitor

app = Flask(__name__)

@app.route("/addinformurl", methods=["POST"])
def AddInformURL():

    url = request.form["url"]

    WaterSupplyMonitor.AddInfomURL(url)

