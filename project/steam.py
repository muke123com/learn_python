# -*-coding:utf-8-*-
import requests
import json
import lxml.html
import pymysql

etree = lxml.html.etree


class Steam(object):
    def __init__(self):
        self.headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.13.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "ff722f12-1ce1-4cfe-a8b5-d82599eeac92,b3dc6884-ec05-4f31-b289-839ecb914be7",
            'Host': "store.steampowered.com",
            'cookie': "browserid=1416852338436325107; timezoneOffset=28800,0; _ga=GA1.2.463066502.1553165097; lastagecheckage=1-0-1989; recentapps=%7B%22359320%22%3A1565690459%2C%221061090%22%3A1565334951%2C%221065200%22%3A1564637985%2C%22637650%22%3A1561519235%2C%22426310%22%3A1558613718%2C%22425220%22%3A1558613656%2C%22841370%22%3A1558006753%2C%22587620%22%3A1556331485%7D; steamCountry=CN%7C13852a31b3412e1296f25a9a190eca0d; sessionid=2af43e0f622f21e19081faa1; _gid=GA1.2.2077785393.1566981702; app_impressions=323190@1_7_7_230_150_1|230410@1_7_7_230_150_1|239140:335810:325724:435111:325723:347090@1_7_7_230_150_1|812140@1_7_7_230_150_1|271590@1_7_7_230_150_1|359550@1_7_7_230_150_1|617290@1_7_7_230_150_1|570@1_7_7_230_150_1|578080@1_7_7_230_150_1|730@1_7_7_230_150_1|431960@1_7_7_230_150_1|594650@1_7_7_230_150_1|678950@1_7_7_230_150_1",
            'accept-encoding': "gzip, deflate",
            'content-length': "2762",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        self.payload = {
            'filter': 'topsellers',
            'os': 'win',
            'page': 2
        }

        self.count = 0
        self.post_data = {}
        self.str = ''
        self.url = 'https://store.steampowered.com/search/'
        self.session = requests.session()
        self.search_key = ""

        self.db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='m_test')
        self.cursor = self.db.cursor()

        pass

    def get_data(self, page):
        self.payload['page'] = page
        r = requests.get(self.url, params=self.payload, headers=self.headers)
        text = r.content.decode("utf-8")
        # res = json.loads(r.text);
        # el = '<div class="margin-fix" id="list_videos_recommended_videos_items">23213123</div>';

        element = etree.HTML(text)

        el_list = element.xpath('//div[@id="search_result_container"]/div/a')

        # title_list = element.xpath('//div[@id="list_videos_recommended_videos_items"]//a/@title')
        # href_list = element.xpath('//div[@id="list_videos_recommended_videos_items"]//a/@href')
        # img_list = element.xpath('//div[@id="list_videos_recommended_videos_items"]//a//img/@data-original')
        # result = etree.tostring(text[0], method='text')
        sql_data = []
        for el in el_list:
            name = el.xpath('.//span[@class="title"]/text()')[0]
            image = el.xpath('.//img/@src')[0].encode('utf-8')
            href = el.xpath('./@href')[0]
            game_id = el.xpath('./@data-ds-appid')
            discount = el.xpath('.//div[@class="col search_discount responsive_secondrow"]/span/text()')

            if len(discount) != 0:
                price = el.xpath('.//strike/text()')
                discount = discount[0]
            else:
                price = discount
                discount = 0
                pass
            new_price = el.xpath('.//div/@data-price-final')[0]

            if len(game_id) != 0:
                sql_item = {'name': name, 'discount': discount, 'image': image, 'href': href, 'game_id': str(game_id),
                            'price': str(price), 'new_price': new_price}

                sql_data.append(sql_item)

                pass
            # print(game_id, price)
            pass
        self.save_data(sql_data)
        print('result is: ', len(sql_data))

    def save_data(self, sql_data):
        print("保存到数据库")
        table = 'm_steam'
        data = sql_data[0]
        keys = ', '.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = r'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                              values=values)
        update = r', '.join([" {key} = VALUES({key})".format(key=key) for key in data])
        sql += update
        tuple_list = []
        for data in sql_data:
            tuple_list.append(tuple(data.values()))
        try:
            self.cursor.executemany(sql, tuple_list)
            self.db.commit()
            print(len(sql_data))
        except Exception as e:
            print(e)
            self.db.rollback()
        pass

# if __name__ == '__main__':
#     s = Steam()
#     s.get_data()
