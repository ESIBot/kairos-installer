#!/usr/bin/python3

import requests
import json
import sys
import os
import time

max_retries = 5

try:
    api_url = os.environ['KINTON_API_URL'] + "/api/gateways/register"
    token = "kairos/" + os.environ['RESIN_DEVICE_UUID']
except KeyError as e:
    print ("Undefinded %s" % str(e))
    sys.exit(1)

# Get the kinton UUID
for retries in range(max_retries):
    try:
        raw = requests.post(api_url, data={'mac': token})
        res = json.loads(raw.text)

        if 'error' in res:
            print(res['error']['message'])
            sys.exit(1)

        break
    except ValueError as e:
        if retries < max_retries:
            print("Retrying...")
            time.sleep(10)
        else:
            break

print("Got UUID %s" % res['uuid'])

try:
    kinton_uuid = res['uuid']
    os.system('KINTON_UUID=' +
    kinton_uuid +
    ' envsubst < "/apps/mosquitto/config/conf.d/kinton.template" > "/apps/mosquitto/config/conf.d/kinton.conf"')
except KeyError as e:
    print("Can't get an UUID")
    sys.exit(1)
