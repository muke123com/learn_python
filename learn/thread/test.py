import queue

q = queue.Queue(10)

i = 0
total = 20
arr = [1,3]
while not q.full():
    if i < total:
        q.put(i)
        i += 1
        q.get()
        print(i)
    else:
        break


print(",".join())





