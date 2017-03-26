import urllib.request
import urllib.parse
import re
import time
from pathlib import Path
import socket
import urllib.error


http://startpage.wandoujia.com/five/v3/tabs/tops?start=0&max=6
def get_apk_list():
    base = 'http://apps.wandoujia.com/top/'
    weekly = 'weekly'
    toatal  = 'total'
    noteworthy = 'noteworthy'

        # I dont set ads, privacy, zh and verified. If you want, I can add this function
    # ads = '?ads=1'
    # privacy = '&privacy'
    # zh = 'zh=1'
    # verified = 'verified=1'
    number = int(input('Please input how many apks do you want.'))
    url = base + input('Which kind do you want? Select in weekly, total and noteworthy.)\n') + '?page='

    apk_list = []
    
    if number < 72:
        request = urllib.request.Request(url+str((number//72)+1))
        with urllib.request.urlopen(request,timeout=300) as html:
            htmlcontent = html.read().decode('utf-8')
            apk_re = r'url=(.*?)&amp;pn'
            tmp_list = re.findall(apk_re, htmlcontent)
            for j in range(0,number%72):
                apk_list.append(urllib.parse.unquote(tmp_list[j]))        
    else:
        for i in range(0,number//72): 
            request = urllib.request.Request(url+str((i//72)+1))    
            with urllib.request.urlopen(request,timeout=300) as html:
                htmlcontent = html.read().decode('utf-8')
                apk_re = r'url=(.*?)&amp;pn'
                tmp_list = re.findall(apk_re, htmlcontent)
                for item in tmp_list:
                    apk_list.append(urllib.parse.unquote(item))

        if number//72 != 0:
            request = urllib.request.Request(url+str((number//72)+1))
            with urllib.request.urlopen(request,timeout=300) as html:
                htmlcontent = html.read().decode('utf-8')
                apk_re = r'url=(.*?)&amp;pn'
                tmp_list = re.findall(apk_re, htmlcontent)
                for j in range(0,number%72):
                    apk_list.append(urllib.parse.unquote(tmp_list[j]))
    return apk_list

def download(apk_list):
    error_list = []
    Path('./douban/').mkdir(parents=True)
    i = 0
    for item in apk_list:
        try:
            i += 1
            print(item,i) #see the process of download
            apkfile = urllib.request.urlopen(item,timeout=300)
            with open ('./douban/' + item.split('/')[-1:][0], 'wb') as apk:
                data = apkfile.read()
                apk.write(data)
                data=None
        except Exception as e: #socket.timeout,urllib.error.HTTPError,IncompleteRead
            print(e)
            error_list.append((item,e))
            with open('error.txt','a+') as ef:
                ef.write(item+','+','+str(e)+'\n')
    return error_list

if __name__ == '__main__':
    apk_list = get_apk_list()
    download_return = download(apk_list)
