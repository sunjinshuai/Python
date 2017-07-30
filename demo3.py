import requests
import json
from bs4 import BeautifulSoup
import lxml

url = 'https://chs.meituan.com/'
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'chs.meituan.com',
    'Referer':'https://chs.meituan.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Content-Type':'text/html; charset=UTF-8',
}

# 获取分类
def get_start_links(url):
    html = requests.get(url).text
    #print (html)
    soup = BeautifulSoup(html, 'lxml')
    links = [link.find('div').find('div').find('dl').find('dt').find('a')['href'] for link in soup.find_all('div', class_='J-nav-item')]
    #print (links)
    return links

def get_detail_id(url, headers=headers):
    html = requests.get(url, headers=None).text
    soup = BeautifulSoup(html, 'lxml')
    # loads将json转dict
    content_id = json.loads(soup.find('div',class_='J-scrollloader cf J-hub')['data-async-params'])
    return json.loads(content_id.get('data')).get('poiidList')



def main(url):
     start_url_list = get_start_links(url)
     for j in start_url_list:
         for i in range(1, 11):
            category_url = j+'/all/page{}'.format(i)
            shop_id_list = get_detail_id(category_url, headers=None)
            print (shop_id_list)
#            for shop_id in shop_id_list:
#                 item = get_item_info(url+'shop/{}'.format(shop_id, headers))
#                 item_list.append(items)

if __name__ == '__main__':
    main(url)