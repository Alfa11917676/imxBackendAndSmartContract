import csv
import json

# import pandas as pd
# import requests
#
# url = 'https://api.x.immutable.com/v1/mints?token_address=0x8cc131fd208dd17b8420998217d414028d74877f&user=0xF7b617acA6075909A78cc4921C909b90010E55fd'
#
# csvData = pd.read_csv('NNR.csv')
#
# data1 = len(csvData['senderWalletAddress'])
# header = ['walletAddress','tokenID']
# with open('walletAddressToTokenId.csv','a',encoding='utf-8') as f:
#     writer= csv.writer(f)
#     writer.writerow(header)
#     f.close()
# for i in range(data1):
#     walletAddress = csvData['senderWalletAddress'][i]
#     response = requests.get(url+walletAddress)
#     jsonify = json.loads(response.text)
#     filteredData = jsonify['result']
#     for datas in filteredData:
#         user = datas['user']
#         tokenID= datas['token']['data']['token_id']
#         finalData = [user,tokenID]
#         with open('walletAddressToTokenId.csv','a',encoding='utf-8') as vals:
#                  writer = csv.writer(vals)
#                  writer.writerow(finalData)
#                  vals.close()
#





import random
datas= []
for i in range(40):
    data = (random.randint(1,10000))
    datas.append(data)
print (datas)
# print ('0x8cc131fd208dd17b8420998217d414028d74877f'.lower())