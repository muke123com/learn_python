import requests
import time
import json
import pymysql
from lxml import etree

# headers = {
#     'Cookie': '',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# cookie = open('cookie.txt', 'r').read()

# 爬取内容
# headers['Cookie'] = cookie
# r = requests.get('https://www.quandashi.com/', headers=headers)
# f = open('../files/1.html', 'w', encoding='utf-8')
# f.write(r.text)

# 爬取保存图片二进制数据
# r = requests.get('https://github.com/favicon.ico', headers=headers)
# f = open('../files/1.ico', 'wb')
# f.write(r.content)

# post请求
# data = {
#     'name': 'germey',
#     'age': 23
# }
# r = requests.post('http://httpbin.org/post', data=data)
#
# # 上传文件
# data = {
#     'files': open('../files/1.ico', 'rb')
# }
# r = requests.post('http://httpbin.org/post', data=data)

# if r.status_code == requests.codes.ok:
#     print('成功')
#     print(r.text)

# # 模拟登录
# class Login(object):
#     def __init__(self):
#         self.headers = {
#             'Referer': 'http://login.qds.com/',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#             'Host': 'login.qds.com'
#         }
#         self.login_url = 'http://login.qds.com'
#         self.post_url = 'http://login.qds.com/passport/dologin'
#         self.logined_url = 'http://home.qds.com/home/index'
#         self.gee_url = 'http://login.qds.com/passport/gee-test-code'
#         self.session = requests.Session()
#
#     def token(self):
#         res = self.session.get(self.login_url, headers=self.headers)
#         selector = etree.HTML(res.text)
#         token = selector.xpath('//input[2]/@value')[0]
#         return token
#
#     def login(self, adminAccount, adminPwd):
#         t = int(time.time())
#         post_data = {
#         }
#         resLogin = self.session.post(self.post_url, data=post_data, headers=self.headers)
#
#         resPage = self.session.get(self.logined_url, headers=self.headers)
#         pass
#
# if __name__ == '__main__':
#     login = Login()

# mysql
class Blibli(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        self.data_url = 'https://space.bilibili.com/ajax/member/getSubmitVideos'
        self.author_url = 'https://api.bilibili.com/x/relation/stat'
        self.session = requests.session()

        self.db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='m_learn')
        self.cursor = self.db.cursor()

        # 爬取参数
        self.mid = 9717562  # up id
        self.lowest_fans = 100000  # 最低粉丝数

    def getVideo(self, page):
        post_data = {
            'mid': self.mid,
            'tid': 0,
            'page': page,
            'pageSize': 30,
            'keyword': '',
            'order': 'pubdate'
        }
        res = self.session.get(self.data_url, params=post_data, headers=self.headers)
        res = json.loads(res.text)
        if(res['status']):
            vlist = res['data']['vlist']
            self.saveVideo(vlist)
            # f = open('../1.json', 'a+', encoding='utf-8')
            # f.write(json.dumps(vlist, ensure_ascii=False))


        pass

    def saveVideo(self, data_list):
        table = 'b_video'
        if(len(data_list) > 0):
            data = data_list[0]
            keys = ', '.join(data.keys())
            values = ','.join(['%s'] * len(data))
            sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                                 values=values)
            update = ', '.join([" {key} = VALUES({key})".format(key=key) for key in data])
            sql += update
            t_data = []
            for data in data_list:
                t_data.append(tuple(data.values()))

            try:
                self.cursor.executemany(sql, t_data)
                self.db.commit()
                print('***')
            except Exception as e:
                print(e)
                self.db.rollback()

    def getAuthorId(self, mid):
        post_data = {
            'vmid': mid
        }
        res = self.session.get(self.author_url, params=post_data, headers=self.headers, timeout=1000)
        if(res.ok):
            res = json.loads(res.text)
            data = res['data']
            self.saveAuthor(data)
        else:
            print(res.status_code)
            return False
        pass

    def saveAuthor(self, data):
        table = 'b_author'
        mid = int(data['mid'])
        follower = data['follower']
        if follower > self.lowest_fans:
            print(mid)
            sql = 'INSERT INTO {table}(mid) VALUES ({mid}) ON DUPLICATE KEY UPDATE mid = {mid}'.format(table=table, mid=mid)
            try:
                self.cursor.execute(sql)
                self.db.commit()
                print("#")
            except Exception as e:
                print(e)
                self.db.rollback()
        pass

    def run(self):
        for i in range(1):
            self.getVideo(i)

        # for i in range(1000):
        #     print(i)
        #     mid = 9717470 + i
        #     if self.getAuthorId(mid) == False:
        #         break

        self.db.close()
    pass

if __name__ == '__main__':
    b = Blibli()
    b.run()
