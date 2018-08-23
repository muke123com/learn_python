import pymysql
import requests

mid = 1

post_data = {
    'vmid': mid
}
res = requests.get('https://api.bilibili.com/x/relation/stat', params=post_data)

pass
