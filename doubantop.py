import json
import urllib.request
import urllib.error
import gzip
from pathlib import Path
import time

def get_number():
    number = int(input('Please input how many apks do you want.'))
    test_url = 'http://startpage.wandoujia.com/five/v3/tabs/tops?start='+str(number-1)+'&max=6'
    try:
        request = urllib.request.Request(test_url)
        with urllib.request.urlopen(request,timeout=300) as content:
            json_content = gzip.decompress(content.read()).decode('utf-8')
            data = json.loads(json_content)
        if data['entity'][0]['template_type'] == "END":
            number = 'TOO_BIG'
        else:
            number = number
    except Exception as e:
        number = 'TOO_BIG'
        print(e)
    return number


def top_api(number):
    top_list = []
    base_url = 'http://startpage.wandoujia.com/five/v3/tabs/tops?start='
    suffix = '&max=6'
    if number == 'TOO_BIG':
        print('don\'t have too many apps')
    else:
        for i in range(0,(number//6)):
            url = base_url + str(i*6) + suffix
            top_list.append(url)
        if (number%6) != 0:
            url = base_url + str(number//6*6) +'&max=' +str(number%6)
            top_list.append(url)
    return top_list

def parse_json(top_list):
    apk_list = []
    for item in top_list:
        request = urllib.request.Request(item)
        with urllib.request.urlopen(request,timeout=300) as content:
            json_content = gzip.decompress(content.read()).decode('utf-8')
            data = json.loads(json_content)
            for i in range(0,len(data['entity'])):
                package_name = data['entity'][i]['detail']['app_detail']['package_name']
                download_url = data['entity'][i]['detail']['app_detail']['apk'][0]['download_url']['url']
                apk_list.append((package_name,download_url))
    for i in range(0,len(apk_list)):
        if len(str(i+1)) == 1:
            prefix = '00'+ str(i+1) + '_'
        if len(str(i+1)) == 2:
            prefix = '0'+ str(i+1) + '_'
        if len(str(i+1)) == 3:
            prefix = str(i+1) + '_'
        apk_list[i]=(prefix+apk_list[i][0]+'.apk',apk_list[i][1])
    
    return apk_list

def download_apk(apk_list):
    path = './' + time.ctime().replace(' ','_') +'/'
    Path(path).mkdir(parents=True)
    error_list = []
    for item in apk_list:
        print(item[0])
        try:
            request = urllib.request.Request(item[1])
            with urllib.request.urlopen(request,timeout=300) as apkfile:
                with open (path + item[0], 'wb') as apk:
                    data = apkfile.read()
                    apk.write(data)
                    data=None
        except Exception as e:
            print(e)
            error_list.append((item,e))
    return error_list

if __name__ == '__main__':
    number = get_number()
    top_list = top_api(number)
    apk_list = parse_json(top_list)
    download_apk(apk_list)
