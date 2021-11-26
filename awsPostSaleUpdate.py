
import requests
import pandas as pd
import json
tokens = []

id = pd.read_csv('finalTokens.csv')
idsLength = len(id['tokenIds'])
for token in id['tokenIds']:
    tokens.append(token)


for ids in tokens:
    print (f'Starting to upload {ids}')
    Item = {'tokenId': str(ids), 'isAvaiable':'false'}
    postSaleUrl = 'https://5m7llgnq66.execute-api.us-east-2.amazonaws.com/token/token'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url=postSaleUrl, data=json.dumps(Item))
    print (response.text)

print(len(tokens))
print ('Done')