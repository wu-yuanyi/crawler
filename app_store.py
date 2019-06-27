import urllib.request
from bs4 import BeautifulSoup

letter_url_list = []
app_list = []
vay_list = []
bank_list = []

finance_url= 'https://apps.apple.com/vn/genre/ios-finance/id6015'
request = urllib.request.Request(finance_url)
with urllib.request.urlopen(request, timeout=500) as html:
    htmlcontent = html.read().decode('utf-8')
finance_soup = BeautifulSoup(htmlcontent, 'html.parser')

alpha_ul_list = finance_soup.find_all(name='ul',attrs={"class":"list alpha"})[0]
for item in alpha_ul_list:
    if item.text == '#':
        letter_url_list.append('https://apps.apple.com/vn/genre/ios-finance/id6015?letter=*')
    else:
        letter_url_list.append('https://apps.apple.com/vn/genre/ios-finance/id6015?letter=' + item.text)

for letter_url in letter_url_list:
    page_num = 1
    last_app = None
    while True:
        url = letter_url + '&page=' + str(page_num) + '#page'
        print(url)
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request, timeout=500) as html:
            htmlcontent = html.read().decode('utf-8')
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        div = soup.find_all(name='div',attrs={"class":"grid3-column"})[0]
        li = div.find_all(name="li")
        if len(li) == 0:
            break
        else:
            page_num += 1
            if last_app == li[-1].text:
                break
            else:
                last_app = li[-1].text
                for item in li:
                    #if 'Vay tiền online' in item.text:
                    app_list.append(item.text)
