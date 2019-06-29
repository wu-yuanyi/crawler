import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd


def ios_popular(url, keyword_list):
    app_dict = {}
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request, timeout=500) as html:
        htmlcontent = html.read().decode('utf-8')
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    div = soup.find_all(name='div',attrs={"class":"grid3-column"})[0]
    li = div.find_all(name="li")
    for item in li:
        flag = False
        for keyword in keyword_list:
            if keyword in item.text.lower():
                flag = True
                break
        if flag:
            app_dict[item.text] = item.a.get('href')
    return app_dict
            

def ios_like(url):
    url = url + '#see-all/customers-also-bought-apps'
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request, timeout=500) as html:
        htmlcontent = html.read().decode('utf-8')
    like_soup = BeautifulSoup(htmlcontent, 'html.parser')
    script = like_soup.find_all(name='script', attrs={"id":"shoebox-ember-data-store"})[0].text
    re1 = r'customersAlsoBoughtApps":{"data":\[(.*?)\]},"reviews"'
    tmp = re.findall(re1, script)[0]
    re2 = r'"id":"(.*?)"}'
    id_list = re.findall(re2, tmp)
    return id_list


def ios_name(idset):
    name_list = []
    for item in idset:
        url = 'https://apps.apple.com/vn/app/id' + item
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request, timeout=500) as html:
            htmlcontent = html.read().decode('utf-8')
        name_soup = BeautifulSoup(htmlcontent, 'html.parser')
        name = name_soup.find(name='title').text[1:-17]
        name_list.append(name)
        print(name)
    return name_list



if __name__ == '__main__':
    #ios
    ios_url= 'https://apps.apple.com/vn/genre/ios-finance/id6015'
    ios_app_dict = ios_popular(ios_url, ['vay', 'dong'])
    ios_id_set = set()
    for item in ios_app_dict:
        ios_id_list = ios_like(ios_app_dict[item])
        ios_id_set = ios_id_set.union(set(ios_id_list))
    ios_name_list = ios_name(ios_id_set)
    df = pd.DataFrame(ios_name_list, columns=['ios app name'])
    df.to_csv('/Users/wuyuanyi/quark/crawler/ios.csv', encoding='utf-8')
