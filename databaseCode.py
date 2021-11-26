import json
import csv
with open ('latest_IMX_punks.json', 'r') as f:
    data = json.load(f)
val =  data['result']
headers = ['walletAddress','tokenIds']
with open('finalData.csv','a',encoding='utf8') as f:
    writer= csv.writer(f)
    writer.writerow(headers)
ii = 0
for i in val:
    with open('finalData.csv', 'a', encoding='utf8') as f:
        writer = csv.writer(f)
        data = [i['user'],(i['token']['data']['token_id'])]
        writer.writerow(data)
    ii += 1
  #  with open('finalTokenIds.txt','a') as f:
   #     f.write((i['token']['data']['token_id'])+'\n')

print (ii)
