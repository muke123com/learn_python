import threading
import time
import queue
import steam as steam


# 多线程爬取数据
# p 页数
class MyThread(threading.Thread):
    def __init__(self, thread_id, p):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.p = p

    def run(self):
        print("开始线程：" + self.thread_id)
        process_data(self.p)
        print("退出线程：" + self.thread_id)


def process_data(p):
    s = steam.Steam()
    s.get_data(p)
    pass


threads = []
for i in range(1, 20):
    thread = MyThread("t_" + str(i), i)
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print("爬取结束")
