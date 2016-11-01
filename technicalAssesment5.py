import json
import requests
import datetime
from datetime import timedelta
import dateutil.parser

first_endpoint = 'http://challenge.code2040.org/api/dating'
second_endpoint = 'http://challenge.code2040.org/api/dating/validate'
token = 'd6e8cc3d628276b7416906ce28774a6a'

data = {'token' : token}
head = {'content-type': "application/json"}

request = requests.post(first_endpoint, data = json.dumps(data), headers = head)

responseDict = json.loads(request.content)

date = dateutil.parser.parse(responseDict['datestamp'], ignoretz = True)

date += timedelta(seconds = responseDict['interval'])

date = date.isoformat() + 'Z'

validateData = {'token': token, 'datestamp': date}
validateRequest = requests.post(second_endpoint, data = json.dumps(validateData), headers = head)

print validateRequest.text
