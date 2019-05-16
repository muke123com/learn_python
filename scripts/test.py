import requests
import json
import lxml.html
import pymysql
etree = lxml.html.etree

url = ""

payload = {
    'mode':'async',
    'function':'get_block',
    'block_id':'list_videos_videos_list_search_result',
    'q':'',
    'category_ids':'',
    'sort_by':'',
    'from_videos':'02',
    'from_albums':'02',
    '_':1558014199821
}
headers = {
    'Content-Type': "application/json",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 115Browser/9.1.1",
    # 'Accept': "*/*",
    # 'Cache-Control': "no-cache",
    # 'Postman-Token': "e7e7eb75-0fef-4a28-8d3b-235c67370432,635be8fe-9bde-4810-b9ad-06438e8372dd",
    'Host': "www.femdomtb.com",
    # 'accept-encoding': "gzip, deflate",
    # 'content-length': "1531",
    # 'Connection': "keep-alive",
    # 'cache-control': "no-cache"
    }

r = requests.get(url, data=payload, headers=headers);
r.encoding = "utf-8"
# res = json.loads(r.text);
# el = '<div class="margin-fix" id="list_videos_recommended_videos_items">23213123</div>';
element = etree.HTML(r.text)
title_list = element.xpath('//div[@id="list_videos_recommended_videos_items"]//a/@title')
href_list = element.xpath('//div[@id="list_videos_recommended_videos_items"]//a/@href')
img_list = element.xpath('//div[@id="list_videos_recommended_videos_items"]//a//img/@data-original')
# result = etree.tostring(text[0], method='text')
for title in img_list:
    print(title);
    pass;
print ('result is: ', len(img_list));
# print(r.text);

