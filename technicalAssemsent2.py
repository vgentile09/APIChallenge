import json
import requests

first_endpoint = 'http://challenge.code2040.org/api/reverse'
second_endpoint = 'http://challenge.code2040.org/api/reverse/validate'
token = 'd6e8cc3d628276b7416906ce28774a6a'

data = {'token' : token}
head = {'content-type': "application/json"}

request = requests.post(first_endpoint, data = json.dumps(data), headers = head)

#print request.text

textToReverse = request.text
reverseText = textToReverse[::-1]

reversedData = {'token' : token, 'string' : reverseText}

validateRequest = requests.post(second_endpoint, data = json.dumps(reversedData), headers = head)

print validateRequest.text

