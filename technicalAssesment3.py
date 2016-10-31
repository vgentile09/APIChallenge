import json
import requests

first_endpoint = 'http://challenge.code2040.org/api/haystack'
second_endpoint = 'http://challenge.code2040.org/api/haystack/validate'
token = 'd6e8cc3d628276b7416906ce28774a6a'

data = {'token' : token}
head = {'content-type': "application/json"}

request = requests.post(first_endpoint, data = json.dumps(data), headers = head)

#print request.text

responseData = request.content
responseDict = json.loads(responseData)

index = responseDict["haystack"].index(responseDict["needle"])

indexData = {'token' : token, 'needle' : index}

validateRequest = requests.post(second_endpoint, data = json.dumps(indexData), headers = head)

print validateRequest.text
