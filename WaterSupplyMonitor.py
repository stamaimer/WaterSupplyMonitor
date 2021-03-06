# -*- coding: utf-8 -*-

__author__ = 'stamaimer'

import os
import re
import requests

from celery import Celery

celery = Celery("WaterSupplyMonitor", broker="amqp://guest:guest@localhost:5672//", backend="rpc://")

celery.config_from_object("config")

PLANED_WATER_CUT_REGEX = '<a href="./jhxts/.+?.htm" target="_blank">.+?</a>'
SUDDEN_WATER_CUT_REGEX = '<a href="./tfxts/.+?.htm" target="_blank">.+?</a>'

SOURCE_URL = "http://www.whwater.com/gsfw/tstz/"

INFORM_URL = ["http://sc.ftqq.com/SCU436T08f5357b0dafad0249283e67c3b4e71f55f677ffe2b28.send"]

keywords = ["东湖", "珞狮", "珞瑜", "广八路", "八一路", "卓刀泉", "水果湖"]

last_message = ""

inform_urls = open("inform_urls.txt", "r")

INFORM_URL.extend(inform_urls.read().split(os.linesep)[:-1])

for url in INFORM_URL:

    print url

inform_urls.close()

@celery.task
def QueryWaterCutInfo():

    message = []

    response = requests.get(SOURCE_URL)

    if response.status_code == 200:

        results = re.findall('|'.join([PLANED_WATER_CUT_REGEX, SUDDEN_WATER_CUT_REGEX]), response.content)

        for result in results:

            tmp = re.findall("<a.+?>.+?</a>", result)[1]

            url = re.findall("\./.+?\.htm", tmp)[0][2:]

            msg = re.findall(">.+?<", tmp)[0][1:-1]

            msg = '[' + msg + ']' + '(' + SOURCE_URL + url + ')'

            print msg

            for keyword in keywords:

                if keyword in msg:

                    message.append(msg)

                    break

        if message == []:

            return

        message = "\n\n".join(message)

        global last_message

        if message == last_message:

            return

        last_message = message

        payload = {"text": "停水通知", "desp": message}

        for url in INFORM_URL:

            print url

            response = requests.post(url, data=payload)

            print response.status_code


@celery.task
def AddInfomURL(url):

    print url

    INFORM_URL.append(url)

    inform_urls = open("inform_urls.txt", 'a')

    inform_urls.write(url + os.linesep)

    inform_urls.close()

    # 持久化到文件还是DataBase