import requests
import pandas as pd
import json
import csv

downloaded_copy = pd.read_excel('fms.xlsx')

#pranavCopyLength = len(pranavCopy['senderWalletAddress'])
downloaded_copyLength = len(downloaded_copy['Deserve one'])

address = {}
walletAddressListMinted = []
totalAddresses=[]
for i in range(downloaded_copyLength):
    vals =  []
    url = 'https://api.x.immutable.com/v1/mints?token_address=0x8cc131fd208dd17b8420998217d414028d74877f&user='
    walletAddress = downloaded_copy['Deserve one'][i]

    response = requests.get(url + walletAddress)
    jsonnify = json.loads(response.text)
    if jsonnify['result'] == []:
        print(walletAddress)
    totalDatas = jsonnify['result']  # [3][1]
    totalAddresses.append(walletAddress)
headers = ['tokenIds']
with open('fmsTokens.csv', 'a', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for datas in totalDatas:
        try:
            pass
        except :
            print ('printint in except')
            print (walletAddress)
        if walletAddress not in walletAddressListMinted:
            walletAddressListMinted.append(walletAddress)
            with open('finalData.csv', 'a', encoding='utf8') as f:
                writer = csv.writer(f)
                data = [(datas['token']['data']['token_id'])]
                writer.writerow(data)
            vals.append([datas['token']['data']['token_id']])
            address[walletAddress] = vals
print (address)
# pranavCopyAddress = []
# for i in range(pranavCopyLength):
#     wallet = pranavCopy['senderWalletAddress'][i]
#     pranavCopyAddress.append(wallet)
# addressestoMint = []

# for uniqueaddress in pranavCopyAddress:
#     if uniqueaddress not in address:
#         addressestoMint.append(uniqueaddress)
#     else:
#         pass
# finalList = []
# for addresses in addressestoMint:
#     if addresses in totalAddresses:
#         finalList.append(addresses)
#     else :
#         pass
# print (finalList)
# print (len(addressestoMint))