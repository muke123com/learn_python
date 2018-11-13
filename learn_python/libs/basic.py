class Basic:
    def __init__(self):
        self.num = 111
        self.str = 'abcdefg'
        self.list = [3, 1, 5, 2, 5]
        self.tup = (1, 2, 3.4, 'a', 'c')
        self.dict = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
        }
        self.set1 = set('abcdefgh')
        self.set2 = set('abcd12345efgh')
        self.data = {
            'comment': 304,
            'typeid': 171,
            'play': 22555,
            'pic': '//i2.hdslb.com/bfs/archive/70dc503e4ec15a0511226ff6b9be0ed6bc61d4e3.png',
            'subtitle': '',
            'description': '(=・ω・=)再次说下，因为无缝连接，导致视频多次花屏，我已经尽最大努力去修复了，但是还是有一小部分视频是花屏的，只能听声音。这个我实在是没有办法，因为他们无缝连接的时候并不会通知，都是很突然的就换人推流了。',
            'copyright': '',
            'title': '【星际老男孩】8月8号GSL选人仪式+天梯+魔兽+三国战纪+街机+快递',
            'review': 0,
            'author': '星际老男孩',
            'mid': 9717562,
            'created': 1533790912,
            'length': '425:19',
            'video_review': 1077,
            'favorites': 43,
            'aid': 28901896,
            'hide_click': False
        }

    def test(self):
        print(self.set2 - self.set1)
        print('=========================== 集合 =============================')
        if self.num > 0:
            print(str(self.num) + '大于0' )
        print('=========================== 判断 =============================')
        for index, item in enumerate(self.list):
            print(str(index) + '-' + str(item))
        print('=========================== 循环 =============================')
        # 迭代
        it = iter(self.list)
        print(next(it))
        print(next(it))
        print('=========================== 迭代 =============================')
        list = self.list
        print(list.count(1), list.count(5), list.count(9))
        list.append(5)
        list.insert(0, -1)
        print(list)
        print(list.index(5))
        list.reverse()
        print(list)
        list.sort()
        print(list)
        list2 = [num**2 for num in list]
        print(list2)
        print('=========================== 数组 =============================')
        tp = tuple(self.data.values())
        tp2 = tp*2
        t_data = self.data.values()
        print('=========================== json =============================')

        pass

    def nine(self):
        i = 1
        while(i <= 9):
            j = 1
            while(j <= i):
                print('\033[1;35m' + str(j) + '*' + str(i) + '=' + str(i*j) + '\033[0m', end=' ')
                j += 1
            i += 1
            print('\n')

        pass
