import urllib.request
import urllib.parse
import urllib.error
import json
import time
#from socket import timeout
#import re
url = 'http://www.bjp2p.com.cn/malice/queryMaliceList'

page = 1
length = 1
infoList = []
while length != 0:
    print(page)
    values = {'name':'','idcardno':'','isLoss':'','province':'',
    'hasCollection':'','page':page,'num':500}
    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request, timeout=300) as html:
        htmlcontent = html.read().decode('utf-8')
    maliceList = json.loads(htmlcontent)['maliceList']
    length = len(maliceList)
    for item in maliceList:
        tmp = [item['name'], item['idcardno'], item['phoneNo'], item['province'], 
        str(item['totalLoanAmount']), item['overdue'], item['beginOverdueTime'], item['isLoss'], 
        item['hasCollectionDesc'], item['hasCollection'], item['platFormName'], str(item['id'])]
        infoList.append(','.join(tmp))
    page += 1
    with open('/Users/wuyuanyi/workspace/test/bjp2p.txt', 'a') as file:
        for item in infoList:
            file.write(item+'\n')
    infoList = []