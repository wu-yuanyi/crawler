#爬发卡行识别码

import urllib.request
import urllib.parse
import urllib.error
import re
import time
from socket import timeout

def get_bin_list():
    url1='http://www.chakahao.com/cardbin/chakahao_icbc.html'
    url2='http://www.chakahao.com/cardbin/chakahao_jt.html'
    url3='http://www.chakahao.com/cardbin/chakahao_ccb.html'
    url4='http://www.chakahao.com/cardbin/chakahao_abc.html'
    url5='http://www.chakahao.com/cardbin/chakahao_boc.html'
    url6='http://www.chakahao.com/cardbin/chakahao_zs.html'
    url7='http://www.chakahao.com/cardbin/chakahao_psbc.html'
    url8='http://www.chakahao.com/cardbin/chakahao_other.html'
    bank_list = [url1, url2, url3, url4, url5, url6, url7, url8]
    bank_bin_list = []
    for item in bank_list:
        request = urllib.request.Request(item)
        try:
            with urllib.request.urlopen(request,timeout=300) as html:
                htmlcontent = html.read().decode('gb2312')
        except timeout:
            print(url+' timeout')
        bin_re = r"target='_blank'>(.*?)</a>"
        tmp = re.findall(bin_re, htmlcontent)
        bank_bin_list.append(tmp)
    return bank_bin_list


def get_bin_info(bank_bin_list):
    base = 'http://www.chakahao.com/cardbin/html/'
    for bank in bank_bin_list:
        for item in bank:
            url = base + item + '.html'
            request = urllib.request.Request(url)
            try:
                with urllib.request.urlopen(request,timeout=300) as html:
                    htmlcontent = html.read().decode('gb2312')
            except timeout:
                print(item + ' timeout')
            re1 = r'开头的银行卡是(.*?)</p>'
            re2 = r'开头的银行卡类型是(.*?)</p>'
            re3 = r'开头的银行卡号数字长度为(.*?)如：'
            tmp1 = re.findall(re1, htmlcontent)[0]
            tmp2 = re.findall(re2, htmlcontent)[0]
            tmp3 = re.findall(re3, htmlcontent)[0]
            line = tmp1 + ',' + tmp2 + ',' + tmp3 + '\n'
            with open('./store.csv','a') as store_file:
                store_file.write(line)



if __name__ == '__main__':
    bin_list = get_bin_list()
    get_bin_info(bin_list)
