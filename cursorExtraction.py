import requests
import json
import csv
tokenNumbers = 0
remaining = 1
tokensToCount = {}
tokenList = []
url = 'https://api.x.immutable.com/v1/mints?token_address=0x8cc131fd208dd17b8420998217d414028d74877f&cursor='
while remaining == 1:
    response = requests.get(url)
    jsonifiedData = json.loads(response.text)
    datas = jsonifiedData['result']
    for data in datas:
        tokenNumbers += 1
        tokenList.append(data['token']['data']['token_id'])
    values = jsonifiedData['cursor']
    url ='https://api.x.immutable.com/v1/mints?token_address=0x8cc131fd208dd17b8420998217d414028d74877f&cursor='+str(values)
    remaining = int(jsonifiedData['remaining'])
for ids in tokenList:
    if ids not in tokensToCount:
        tokensToCount[ids] = 1
    else:
        tokensToCount[ids] = tokensToCount[ids]+1
headers = ['tokenIds']
with open('finalUpload.csv','a',encoding='utf8') as f:
    writer= csv.writer(f)
    writer.writerow(headers)
for ids in tokenList:
    with open('finalUpload.csv','a', encoding='utf8') as f:
        writer = csv.writer(f)
        data = [ids]
        writer.writerow(data)
# print (sorted(tokenList[0]))
#print (tokensToCount)
print (f'The tokenNumbers total fetched is {tokenNumbers}')