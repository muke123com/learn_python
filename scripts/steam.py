import requests
import json
import lxml.html
import pymysql
etree = lxml.html.etree

url = "https://store.steampowered.com/search/"

payload = {
    'filter':'topsellers',
    'os':'win'
}
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "ff722f12-1ce1-4cfe-a8b5-d82599eeac92,b3dc6884-ec05-4f31-b289-839ecb914be7",
    'Host': "store.steampowered.com",
    'cookie': "browserid=1236714060563709583; steamCountry=US%7C432f4111787c32105042ed9af4173078; sessionid=82412d35c1508e59c1703b5f",
    'accept-encoding': "gzip, deflate",
    'content-length': "2762",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

# r = requests.get(url, data=payload, headers=headers);
r = {
    'text': ''
}
# r.encoding = "utf-8"
# res = json.loads(r.text);
# el = '<div class="margin-fix" id="list_videos_recommended_videos_items">23213123</div>';

r['text'] = open('scripts/1.html', 'r', encoding="utf-8").read();

element = etree.HTML(r['text'])

el_list = element.xpath('//div[@id="search_result_container"]/div/a')

# title_list = element.xpath('//div[@id="list_videos_recommended_videos_items"]//a/@title')
# href_list = element.xpath('//div[@id="list_videos_recommended_videos_items"]//a/@href')
# img_list = element.xpath('//div[@id="list_videos_recommended_videos_items"]//a//img/@data-original')
# result = etree.tostring(text[0], method='text')
for el in el_list:
    name = el.xpath('.//span[@class="title"]/text()')[0].encode('utf-8')
    image = el.xpath('.//img/@src')[0].encode('utf-8')
    href = el.xpath('./@href')[0]
    game_id = el.xpath('./@data-ds-appid')
    discount = el.xpath('.//div[@class="col search_discount responsive_secondrow"]/span/text()')

    if(len(discount) != 0):
        price = el.xpath('.//strike/text()')
        discount = discount[0]
    else:
        price = discount
        discount = 0
        pass
    new_price = el.xpath('.//div/@data-price-final')[0]
    if(len(game_id) != 0):
        sql_item = {}
        sql_item['name'] = name;
        sql_item['discount'] = discount;
        sql_item['image'] = image;
        sql_item['href'] = href;
        sql_item['game_id'] = game_id;
        sql_item['price'] = price;
        sql_item['new_price'] = new_price;

        print(sql_item)
        pass

    # print(new_price)
    pass;
print ('result is: ', len(el_list));

