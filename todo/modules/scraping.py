import os
import sys
from urllib import request as req
from urllib import error
from urllib import parse
import bs4
import requests as reqs

def get_html(keyword): 
    url = 'https://alert.shop-bell.com/search/?safesearch=&safesearch[]=1&Books=1&BrowseNode=&Title=' + keyword + '&Author=&Publisher=&BooksSelectedBn=指定なし&bnBooksLv_1='
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}
    request = req.Request(url = url, headers = headers)
    page = reqs.get(url, timeout = 2000)
    return page.content

def parse_html(page):
    html = bs4.BeautifulSoup(page, 'html.parser')
    elems = html.select('td')
    
    #前の巻と発売日
    prev = elems[1].contents[0]
    prev_release = elems[1].contents[2].replace('年','-').replace('月','-').replace('日','').replace(' 発売','')

    #次の巻
    nxt = elems[2].contents[0]
    nxt_release = elems[2].contents[2].contents[0].contents[0].replace('年','-').replace('月','-').replace('日','').replace(' 発売予定','')
    
    return prev, prev_release, nxt, nxt_release

def main():
    args = sys.argv
    keyword = args[1]
    page = get_html(keyword)
    parse_html(page, keyword)

if __name__ == '__main__':
    main()
