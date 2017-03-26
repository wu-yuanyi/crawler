import urllib.request
import urllib.parse
import re
import time
from pathlib import Path
import socket
import urllib.error

base = 'http://shouji.baidu.com/rank/'
anchor = 'http://shouji.baidu.com'
grand = 'http://shouji.baidu.com/'
#index1 = ['top/','top/software/','top/game/']
index1 = []
index2 = ['up/']
#index3 = ['features/','features/classic/','features/developer/','features/artistic/']
index3 = []
totalindex = [index1, index2, index3]

def index(totalindex):
    indexdir = {}
    for index in totalindex:
        for page in index:
            request = urllib.request.Request(base+page)
            with urllib.request.urlopen(request,timeout=300) as html:
                htmlcontent = html.read().decode('utf-8')
                name = '_'.join(page.split('/')[0:len(page.split('/'))-1])
                indexdir[name]=htmlcontent
    return indexdir

def link(indexdir):
    linkdir = {}
    for item in sorted(indexdir):
        htmlcontent = indexdir[item]
        listnum_re=r'list_(.*?).html'
        num = re.findall(listnum_re,htmlcontent)
        if num == []:
            rtn = 1
        else:
            intnum = []
            for strnum in num:
                intnum.append(int(strnum))
            rtn = max(intnum)
        linkdir[item] = rtn
    return linkdir

def app(linkdir):
    appdir = {}
    appset = {}
    for item in linkdir:
        itemlis = []
        for num in range(1,linkdir[item]+1):
            itemlis.append(base + ('/').join(item.split('_')) + '/list_' + str(num) +'.html')
        appdir[item] = itemlis
    for category in sorted(appdir):
        categoryapp = []
        for pagelink in appdir[category]:
            #print(pagelink)
            request = urllib.request.Request(pagelink)
            with urllib.request.urlopen(request,timeout=300) as html:
                htmlcontent = html.read().decode('utf-8')
            app_re = r'class="app-box" href="(.*?)">'
            for applink in re.findall(app_re,htmlcontent):
                categoryapp.append(anchor+applink)
            #categoryapp.append(re.findall(app_re,htmlcontent))
        appset[category]=categoryapp
    return appset

def download(appset):
    errorlist=[]
    for item in appset:
        Path('./baidu/' + item).mkdir(parents=True)
        for applink in appset[item]:
            print(applink)
            try:
                request = urllib.request.Request(applink)
                app = (applink.split(grand)[1]).split('.html')[0].replace('/','_')
                with urllib.request.urlopen(request,timeout=300) as html:
                    htmlcontent = html.read().decode('utf-8')
                download_re = r'href="(.*?)"\n[ ]*?class="apk"'
                downloadlink = re.findall(download_re,htmlcontent)[0]
                if downloadlink.startswith('http://down.anzhuo.cn/'):
                    errorlist.append(applink)
                else:
                    apkfile=urllib.request.urlopen(downloadlink,timeout=300) 
                    with open('./baidu/' + item + '/' + app +'.apk','wb') as apk:
                        data = apkfile.read()
                        apk.write(data)
                        data=None
            except Exception as e:#socket.timeout,urllib.error.HTTPError,IncompleteRead
                print(e)
                errorlist.append((item,applink,e))
                with open('error.txt','a+') as ef:
                    ef.write(item+','+applink+','+str(e)+'\n')
    return errorlist

if __name__ == '__main__':
    index_return = index(totalindex)
    link_return = link(index_return)
    app_return = app(link_return)
    download_return = download(app_return)
