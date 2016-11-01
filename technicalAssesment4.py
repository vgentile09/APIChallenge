import json
import requests

first_endpoint = 'http://challenge.code2040.org/api/prefix'
second_endpoint = 'http://challenge.code2040.org/api/prefix/validate'
token = 'd6e8cc3d628276b7416906ce28774a6a'

data = {'token' : token}
head = {'content-type' : "application/json"}

request = requests.post(first_endpoint, data = json.dumps(data), headers = head)

#print request.text

responseData = request.content
responseDict = json.loads(responseData)

arr = responseDict['array']
prefixArray = []

#print arr

for str in arr:
  if str.startswith(responseDict['prefix']) is False:
    prefixArray.append(str)

#print prefixArray
validateData = {'token' : token, 'array' : prefixArray}
validateRequest = requests.post(second_endpoint, data = json.dumps(validateData), headers = head)

print validateRequest.text
