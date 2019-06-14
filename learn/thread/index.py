import threading
import time
import queue

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.q = q

    def run(self):
        print("开始线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


def process_data(thread_name, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (thread_name, data))
        else:
            queueLock.release()
            time.sleep(1)
        pass


thread_list = ["T1", "T2", "T3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
thread_id = 1

for t_name in thread_list:
    thread = MyThread(thread_id, t_name, workQueue)
    thread.start()
    threads.append(thread)
    thread_id += 1


queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()


while not workQueue.empty():
    pass


exitFlag = 1


for t in threads:
    t.join()

print("退出主线程")
