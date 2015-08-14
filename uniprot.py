#-*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import re

str_alias = input("Pleas input Gene names:\ne.g.(OR1D2,OR7D4...)\n")

list_alias = str_alias.split(',')

if (list_alias == ['']):
    list_alias = ['OR1D2','OR7D4','OR1G1','OR1A1','OR1J4','OR1A2','OR2C1','OR2J2','OR2W1','OR2M7','OR2V1','OR3A1','OR4E2','OR4C12','OR5P3','OR5D18','OR6C4','OR51L1','OR51E1','OR51E2','OR52A5','OR52E4','OR52K1','OR52B2','OR52D1','OR10A4','OR10J5','OR10AD1','OR56A5','OR4C45','OR2F2','OR10H4','OR4C3','OR4C13','OR5B2','OR5A1','OR5T2','OR9G4','OR5M8','OR8J1','OR5M3','OR8G2','OR8J3','OR13C4','OR14C36']

url_head = 'http://www.uniprot.org'
def html():
    result_html = {}
    for alias in list_alias:
        request = urllib.request.Request(url_head+"/uniprot/?query="+alias+"&sort=score")
        with urllib.request.urlopen(request) as f:
            str_html = f.read().decode('utf-8')
            str_re = '(href)[^(href)].*?_HUMAN'+'.*?'+'<strong>'+alias
            m = re.search(str_re,str_html).group(0)
            n = re.search('(/.*?")',m).group(0)
            result_html[alias] = url_head + n[:-1]
    #print (result_html)
    return result_html

source = html()

def extra():
    #source = html()
    result_extra = {}
    for item in source:
        request = urllib.request.Request(source[item])
        with urllib.request.urlopen(request) as f:
            str_html = f.read().decode('utf-8')
            str_re = r'(\d{1,4})&nbsp;&ndash;&nbsp;(\d{1,4})</a></td><td class="numeric">(\d{1,4})</td><td><span property="text">Extracellular'
            m = re.findall(str_re,str_html)
            result_extra[item] = m
    #print (result_extra)
    return result_extra

def bond():
    #source = html()
    result_bond = {}
    for item in source:
        request = urllib.request.Request(source[item])
        with urllib.request.urlopen(request) as f:
            str_html = f.read().decode('utf-8')
            str_re = r'</span>Disulfide bond<sup>i</sup></span>.*?(\d{1,4}) &harr; (\d{1,4})'
            m = re.findall(str_re,str_html)
            result_bond[item] = m
    #print (result_bond)
    return result_bond


if __name__ == '__main__':
    print("*****************html*****************")
    print(html())
    print("*****************Extracelluar*****************")
    print(extra())
    print("*****************Disulfide bond*****************")
    print(bond())
