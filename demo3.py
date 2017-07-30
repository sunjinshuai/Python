import requests
import json
from bs4 import BeautifulSoup
import lxml

url = "http://i.meituan.com/"

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'max-age=0',
    'Content-Type':'text/html;charset=UTF-8',
    'Keep-Alive':'timeout: 38',
    'Host':'http://i.meituan.com/',
    'Proxy-Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Mobile Safari/537.36',
}

def get_start_links(url):
    html = requests.get(url).text

    soup = BeautifulSoup()

get_start_links(url)

