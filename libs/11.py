import requests
import json
import time
import os
import lxml.html
import pymysql
etree = lxml.html.etree

class Pic(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.count = 0
        self.post_data = {}
        self.str = ''
        self.data_url = ''
        self.pic_base = ''
        self.files_folder = 'D:/PycharmProjects/images/'
        self.session = requests.session()
        self.search_key = ""

        self.db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='m_learn')
        self.cursor = self.db.cursor()

        pass

    def get_pics(self):
        if self.count > 5:
            return
        key = self.search_key
        key = key.encode(encoding='utf-8')
        self.post_data['query'] = key
        # self.post_data['cursor'] = ''
        post_data = self.post_data
        res = self.session.get(self.data_url, params=post_data, headers=self.headers)
        res = json.loads(res.text)
        data_list = res['data']
        sql_data = []
        for item in data_list:
            sql_item = {}
            sql_item['p_keyword'] = key
            sql_item['p_key'] = item['key']
            tags = item['tags']
            tags_str = ','.join(tags)
            sql_item['p_tags'] = tags_str
            sql_item['p_favorite'] = 0
            sql_item['p_like'] = 0
            if item.get('reactions'):
                sql_item['p_favorite'] = item['reactions'].get('favorite')
                sql_item['p_like'] = item['reactions'].get('like')

            if item['contentType'] == "image/jpeg":
                s = item['transforms']['']
            else:
                s = item['transforms'][':image/jpeg']

            sql_item['p_url'] = s

            sql_data.append(sql_item)

        self.save_pics(sql_data)
        if len(sql_data) < 50:
            return
        self.post_data['cursor'] = res['cursor']

        self.get_pics()

        pass

    def save_pics(self, sql_data):
        table = 'm_pic'
        data = sql_data[0]
        keys = ', '.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                             values=values)
        update = ', '.join([" {key} = VALUES({key})".format(key=key) for key in data])
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

    def download_pics(self):
        sql = "SELECT p_url FROM m_pic WHERE p_tags LIKE '%boot%'"
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print('dddddd')
        except Exception as e:
            print(e)
            self.db.rollback()
        o_count = 0
        d_count = 0
        all_count = len(result)
        for l in result:
            l = "".join(l)
            pic_url = self.pic_base + l
            path = self.files_folder
            if not os.path.exists(path):
                os.makedirs(path)

            has_file = os.path.exists(path + l + '.jpg')
            if not has_file:
                try:
                    r = requests.get(pic_url)
                    d_count += 1

                except requests.exceptions.Timeout:
                    print('timeout')
                    r = requests.get(pic_url)
                    d_count += 1

                with open(path + l + '.jpg', 'wb') as file:
                    file.write(r.content)
                    print('新下载数：' + str(d_count) + ' 总数：' + str(d_count + o_count) + '/' + str(all_count))
            else:
                o_count += 1
    pass

if __name__ == '__main__':
    p = Pic()
    # p.get_pics()
    p.download_pics()
