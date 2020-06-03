# -*- coding: utf-8 -*-
import json
import requests

# Actual request
req = requests.get('http://10.30.20.71:5001/channel/measurement/latest', timeout=10)
data = req.json()
print('Response: \n{}'.format(json.dumps(data, indent=2)))
