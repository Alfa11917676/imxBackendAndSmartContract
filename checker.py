import requests
import json

url = 'https://api.ropsten.x.immutable.com/v1/mintable-token/0x8cc131fd208dd17b8420998217d414028d74877f/'

with open ('pranav.json', 'r') as f:
    data = json.load(f)
val =  data['result']
fig = []

for i in range(10000):
    finalURL = url+str(i)
    response = requests.get(finalURL)
    with open ('logs.txt', 'a')as f:
        f.write(response.text+'\n')
    print (response.text)