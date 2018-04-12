#使用queue对象
#已通过运行测试
from random import randint
from time import sleep
from queue import Queue
from myThread import MyThread

#写
def writeQ(queue):
    print("producing object for Q...")
    queue.put("xxx",1)
    print("sizi now",queue.qsize())

#读
def readQ(queue):
    val = queue.get(1)
    print("consumed object from Q...sizi now",queue.qsize())

#写入控制器
def writer(queue,loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3)) #为了保证队列不为0，写入时间比读取时间更短

#读取控制器
def reader(queue,loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))

funcs = [writer,reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i],(q, nloops),funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print("all DONE")

if __name__ == '__main__':
    main()


