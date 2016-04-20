import urllib.request
import urllib.parse
import re
import xlwt
import time

def login(keyword):
    #print('login')
    keywords='+'.join(keyword.split(' '))
    #data = urllib.parse.urlencode({'type':'publication','query':keyword})
    #data = data.encode('utf-8')
    request = urllib.request.Request("http://www.researchgate.net/search.Search.html?type=publication&query="+keywords)
    #request.eadd_header("authority","www.researchgate.net")
    #request.add_header("method","GET")
    #request.add_header("path","/search.Search.html?type=publication&query="+keywords)
    #request.add_header("accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
    #request.add_header("accept-encoding","gzip, deflate, sdch")
    #request.add_header("accept-language","en-US,en;q=0.8")
    request.add_header("cookie","c1=D%BD%FBv%1D%A4%A8%85%BA%8C%B69%AC%AC%C5%DE%D3%0B%CF%EF%D8%08%8Ff%19%B9c%EF%D7%94Z%CD%83%A0%A0s%25%0C%B0%FA%9D%29WW%2B%8B%29%1AVp%8D0%5B%5E%DBw%84qP%B1%05r%06n; c2=%B9%B7%F2bs5e%FC%17%BFS%90%04%C6%D9%C9%19%2C%049W%F7if%1E%60%D6%B7G%1CSW%F2%B7.W%8D%0F%92%F6%983%93%00%0A%AD7%EEA%D3I%3D%CE%C9%EBI%21%B58p%A3o%CB%FF%15Y%A3%D0.%AEW%ABw%EA%A5%EEN%0F%E9%8A%CE%FFQ%005%E7%CD%24%BA%8F9%E757H%84; sid=cxXjkS1ZyyuEMeQVpA3aMEOYaSolBacHU4R5Xq6Z5juOX0k1mwGc6DxgEJR8hwWg2vII9X3ONV0ozNbt1YZKNLcK4PT62V8EW1Zem1F01ewCAJNk6aS11BA0r3jvgtFv; cili=_2_NTlkODA3ZTFlZWEwZWQwNjI3MDI3MWExZTAxOTBlNWM1YTgwOTkzNDBiZGYzY2ZmNmQ5YzQ5YmFhYWE4OTgyMl8xMDQzNTE5OTsw; cirgu=1; _ga=GA1.2.713749949.1457430856; _gat=1")
    #request.add_header("referer","https://www.researchgate.net/home")
    #request.add_header("upgrade-insecure-requests","1")
    with urllib.request.urlopen(request) as f:
        str_html = f.read().decode('utf-8')
        fhtml = open('./xipeng.html','w')
        fhtml.write(str_html)
        #print(str_html)
        fhtml.close()
    return 'ok'

def nextpage(url):
    request = urllib.request.Request(url)
    request.add_header("cookie","c1=D%BD%FBv%1D%A4%A8%85%BA%8C%B69%AC%AC%C5%DE%D3%0B%CF%EF%D8%08%8Ff%19%B9c%EF%D7%94Z%CD%83%A0%A0s%25%0C%B0%FA%9D%29WW%2B%8B%29%1AVp%8D0%5B%5E%DBw%84qP%B1%05r%06n; c2=%B9%B7%F2bs5e%FC%17%BFS%90%04%C6%D9%C9%19%2C%049W%F7if%1E%60%D6%B7G%1CSW%F2%B7.W%8D%0F%92%F6%983%93%00%0A%AD7%EEA%D3I%3D%CE%C9%EBI%21%B58p%A3o%CB%FF%15Y%A3%D0.%AEW%ABw%EA%A5%EEN%0F%E9%8A%CE%FFQ%005%E7%CD%24%BA%8F9%E757H%84; sid=cxXjkS1ZyyuEMeQVpA3aMEOYaSolBacHU4R5Xq6Z5juOX0k1mwGc6DxgEJR8hwWg2vII9X3ONV0ozNbt1YZKNLcK4PT62V8EW1Zem1F01ewCAJNk6aS11BA0r3jvgtFv; cili=_2_NTlkODA3ZTFlZWEwZWQwNjI3MDI3MWExZTAxOTBlNWM1YTgwOTkzNDBiZGYzY2ZmNmQ5YzQ5YmFhYWE4OTgyMl8xMDQzNTE5OTsw; cirgu=1; _ga=GA1.2.713749949.1457430856; _gat=1")
#request.add_header("cookie","_gat=1; c1=P%90%28%03%B1%0E%FC%F9%9A%FCM%5D%83%E4%9FQ%89am%05%FA%F8%C5%18%E0M%B6q%3B%AC%24MtWA%26J9%DCH%AF%F0%84%FA%28%DDUH%1C%40w%00P%99%28%ABIF%2Cf%02T%B6%11; c2=%87%2C%A1%3A%DA%11%12%D6%5E%04%D9ch%DC%15%0AY0i%08%A5%08%9A%9F%0D%A0%D9%F4%BE%8C%3EL%09%D7%EF%22%3F%AA%19%23%FA%08%06%FD%D1SW%40%96%22F%03%D5%80%95%A0%9F%0Dw%2A%22%AF%1F%9D%D0%95%28%88%FDd%D2%1D%DE%A2u%14%E0%A4%C6%88%82%FEU%E8b%E1%1F%0B%CD%0E%06%FD%17%B1%5E%60; sid=O19111XG05YOilhYB7UtffGRnAp1Oae0kUqOHbX1r1c1YCaXGcfQzXRV2sbjSxSKmrS240DWDbK42T0SRAkJLAagr04IwCFixKFHa0N7VkHO1Ej8GqvE9uurFEkLoH05; cili=_2_MGMwNGNmZjQ1ZTUxZGJiNGFkMDI0ZjlkZjIwYmZiMDJjYTNkZjAxMTlmMWQ1NzQ1NDAxZjljMzE5NzJkNDZlY18xMDM2MDYxMTsw; cirgu=1; _ga=GA1.2.713749949.1457430856")
    with urllib.request.urlopen(request) as f:
        str_html = f.read().decode('utf-8')
        f = open('./xipeng.html','w')
        f.write(str_html)
        f.close()
    return 'ok'


def crawler(str_html, keyword, num):
    
    global list_result 
    list_result = []

    title_re = r'<span class="publication-title js-publication-title">(.*?)</span>'
    title_li = re.findall(title_re,str_html)
    #print(title_li)
    
    authors_re = r'<div class="authors">(.*?)</div>'
    authors_li = re.findall(authors_re,str_html)
    #print(authors_li)
    author_li=[]
    for item in authors_li:
        author_re = r'publications-authors">(.*?)</a>'
        author = re.findall(author_re,item)
        author_li.append(author)
    
    next_re =  r'<a class=" navi-next pager-link ajax-page-load" href="(.*?)" data-target-page'
    if(re.findall(next_re,str_html)) != []:
        next_page =('http://www.researchgate.net/' + re.findall(next_re,str_html)[0]).replace('&amp;','&')
    else: 
        next_page = 'finish'
    #finish_re = r'<a class=" navi-next pager-link ajax-page-load" href data-target-page="(.*?)"'
    #finish_page = re.findall(finish_re,str_html)
    #if finish_page == []:
    #    global end_flag 
    #    end_flag = True
    #else:
    #    global end_flag 
    #    end_flag = False
    print (next_page)
    #print (end_flag)
    #dict_onepage = dict(zip(title_li,author_li))
    #print(dict_onepage)

    global gtl
    global gal

    gtl=gtl+title_li
    gal=gal+author_li
    print(title_li)
    print(author_li)
    #print(gtl)
    #print(gal)
    #fresult = open ('./'+keyword+'.txt', 'a')
    #fresult.write('\n**************************\n')
    #fresult.write(str(dict_onepage))
    #fresult.close()
    #print (dict_fan)
    return next_page

def intelligence(keyword):
    #keyword=input("keyword:")
    login(keyword)
    with open ('./xipeng.html') as f:
        str_html = f.read()
        html_code = str_html
    urllink = crawler(html_code, keyword, 0)
    num = 20
    while urllink !='finish' and num<400:
        time.sleep(15)
        nextpage(urllink)
        with open ('./xipeng.html') as f:
            str_html = f.read()
            html_code = str_html
        urllink = crawler(html_code, keyword, num)
        num = num +20


if __name__ =='__main__':
    list_word=['Laboratory Safety']
    #list_word=['Bioterrorism','Biothreat Agents','biodefend','biosurveillance','biotreat','Laboratory Safety','Agro-terrorism','biocontainment']
    #list_word=['biocrime','Biorisk','BioProtection','Biodefense','Biological Warfare','Biological weapons','Biosafety','biosecurity','Biological Threats','biological control']
    #list_word=['Biohazards','Bio surveilliance','Biological Preparedness','BioShield']
    for word in list_word:
        gtl=[]
        gal=[]
        intelligence(word)
        i=0
        workbook = xlwt.Workbook(encoding = 'ascii')
        worksheet = workbook.add_sheet('My Worksheet')
        for item in gtl:
            worksheet.write(i, 0, label = gtl[i])
            worksheet.write(i, 1, label = str(gal[i]))
            #print(gtl[i])
            #print(gal[i])
            i = i+1
        workbook.save(word+'.xls')
        
        gtl=[]
        gal=[]
