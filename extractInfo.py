import requests
import json
import pandas as pd
tokens = 0
punksData = pd.read_excel('punks.xlsx')
length = len(punksData['walletAddress'])
verifyData = pd.read_csv('nnr.csv')
length2 = len(verifyData['senderWalletAddress'])
address = {}
for i in range(length):
    vals = []
    url = 'https://api.x.immutable.com/v1/mints?token_address=0x8cc131fd208dd17b8420998217d414028d74877f&cursor=eyJ0cmFuc2FjdGlvbl9pZCI6MTk1Njc1MjYsInN0YXR1cyI6InN1Y2Nlc3MiLCJldGhlcl9rZXkiOiIweGQ1ZjU1OTc4OGNiY2RjYmIzNjhiYTlkNGZjNDI5OWZhODEzM2NhNzEiLCJUeXBlIjoiRVJDNzIxIiwiSUQiOiIweGEzNjcyOWRkN2FkMzRmZTJmYzFlYWZiM2QxMTU0ZDQ1ZjA0MTEyZDdiZWU3NDYwNTVmYjBiOGRlOTg0OGM0YjYiLCJFUkM3MjFUb2tlbklEIjoiOTIwMiIsIkNvbnRyYWN0QWRkcmVzcyI6IjB4OGNjMTMxZmQyMDhkZDE3Yjg0MjA5OTgyMTdkNDE0MDI4ZDc0ODc3ZiIsIkRlY2ltYWxzIjpudWxsLCJRdWFudGl0eSI6IjEiLCJjcmVhdGVkX2F0IjoiMjAyMS0xMS0xN1QwNjo0Mjo0Ni4wOTYyNTRaIn0'

    walletAddress = punksData['walletAddress'][i]
   
    response = requests.get(url+walletAddress)
    jsonnify = json.loads(response.text)
   
    totalDatas = jsonnify['result']#[3][1]
    j = 0
    if walletAddress in verifyData['senderWalletAddress']:
        j+=1
    for datas in totalDatas:
        tokens+=1
        vals.append([datas['token']['data']['token_id']])
        address[walletAddress] =  vals

print (address)
print (len(address))
print (j)
print (tokens)