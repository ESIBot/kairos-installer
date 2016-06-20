#!/usr/bin/python3

import requests
import json
import sys
import os
import time
import random
import string

max_retries = 5

api_url        = '' # URL of the API
register_token = '' # Token used on the registration process
kinton_uuid    = '' # Kinton UUID
kinton_dir     = '' # Directory where Kinton is installed

# Get the installation dir
if 'KINTON_DIR' in os.environ:
    kinton_dir = os.environ['KINTON_DIR']
else:
    print('Error: No "KINTON_DIR" defined')
    sys.exit(1)

# Get the API URL
if 'KINTON_API_URL' in os.environ:
    api_url = os.environ['KINTON_API_URL'] + '/api/gateways/register'
else:
    print('Error: No "KINTON_API_URL" provided')
    sys.exit(1)

# Get the register token, if not defined generate a random token
if 'REGISTER_TOKEN' in os.environ:
    register_token = os.environ['REGISTER_TOKEN']
else:
    register_token = ''.join(random.SystemRandom().choice(string.ascii_uppercase
        + string.digits) for _ in range(8))

# Get the kinton UUID
for retries in range(max_retries):
    try:
        raw = requests.post(api_url, data={'mac': register_token})
        res = json.loads(raw.text)

        if 'error' in res:
            print(res['error']['message'])
            sys.exit(1)

        if 'uuid' in res:
            kinton_uuid = res['uuid']
        else:
            exit(1)

        break
    except ValueError as e:
        if retries < max_retries:
            print("Retrying...")
            time.sleep(10)
        else:
            break

# Save UUID to file
target = open(kinton_dir + '/data/uuid', 'w')
target.write(kinton_uuid)
target.close()

print('-----------------------------------------------------------------------')
print('\t\tTOKEN:\t %s' % register_token)
print('\t\tUUID:\t %s' % kinton_uuid)
print('-----------------------------------------------------------------------')
