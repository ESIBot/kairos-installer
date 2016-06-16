#!/usr/bin/python3

import requests
import json
import sys
import os

try:
    api_url = os.environ['KINTON_API_URL'] + "/api/gateways/register"
    token = "kairos/" + os.environ['RESIN_DEVICE_UUID']
except KeyError as e:
    print ("Undefinded %s" % str(e))

# Get the kinton UUID
raw = requests.post(api_url, data={'mac': token})
res = json.loads(raw.text)
print (raw.text)

try:
    kinton_uuid = res['uuid']
    print(os.system('KINTON_UUID=' +
    kinton_uuid +
    ' envsubst < "apps/mosquitto/config/conf.d/kinton.template" > "apps/mosquitto/config/conf.d/kinton.conf"'))
except KeyError as e:
    print("Can't get an UUID")
