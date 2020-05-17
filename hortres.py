import urllib.request
import os
import re 
from bs4 import BeautifulSoup


def get_article(url):
    articles_link = []
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request, timeout=500) as html:
        htmlcontent = html.read().decode('utf-8')
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    articles_div = soup.find_all(name='div',attrs={"class":"in_arts_title"})
    for item in articles_div:
        articles_href = item.find(name='a')['href']
        url = 'http://www.hortres.com/'+articles_href
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request, timeout=500) as html:
            htmlcontent = html.read().decode('utf-8')
        re_text = r'window.open\(\'(.*?)\'\);'
        article_link = re.findall(re_text, htmlcontent)[0]
        articles_link.append(article_link)
    return articles_link


def picture(url):
    words = ['plant', 'flower', 'leaf', 'fruit', 'vegetable', 'tea', 'green', 'mature', 'juvenile', 'grow']
    images = []
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request, timeout=2500) as html:
        htmlcontent = html.read().decode('utf-8')
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    pictures = soup.find_all(name='picture')
    details = soup.find_all(name='div',attrs={"class":"c-article-section__figure-description"})
    length = len(pictures)
    for idx in range(length):
        img = 'http:' + pictures[idx].find_all(name='img')[0]['src']
        try:
            text = str(details[idx].find_all(name='p')[0])
            for item in words:
                if item in text:
                    img_name = './' + img.split('/')[-1]
                    urllib.request.urlretrieve(img, img_name)
                    break
        except:
            print(url)
            pass
    return True


years = ['2019', '2020']
for item in years:
    url = 'http://www.hortres.com/archive.php?volid=' + item
    articles_link = get_article(url)
    for subitem in articles_link:
        picture(subitem)
