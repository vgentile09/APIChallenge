#Code by: Vincent Gentile

import json
import requests

#Connect to the registration endpoint

given_endpoint = 'http://challenge.code2040.org/api/register'
token = 'd6e8cc3d628276b7416906ce28774a6a'
github = 'https://github.com/vgentile09/APIChallenge'

data = {'token': token, 'github': github}

head = {'content-type': "application/json"}

request = requests.post(given_endpoint, data = json.dumps(data), headers = head)

print request.text
