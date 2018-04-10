#模拟糖果机的添加与购买
#已通过运行测试

from atexit import register
from random import randrange
from threading import BoundedSemaphore,Lock,Thread
from time import sleep,ctime

#信号量的实质是计数器，并且BoundedSemaphore永远不会超过它的初始值
lock = Lock()
MAX = 5
candyTray = BoundedSemaphore(MAX)

#装填（注意信号量的逻辑，release释放会增加计数器值）
def refill():
    lock.acquire()
    print("Refilling candy...")
    try:
        candyTray.release()
    except ValueError:
        print("Full,skipping")
    else:
        print("All right,DONE")
    lock.release()

#购买
def buy():
    lock.acquire()
    print("Buying candy...")
    #通过传入非阻塞标志False，让调用不再阻塞，如果返回False指明没有资源
    if candyTray.acquire(False):
        print("OK")
    else:
        print("empty,skiping")
    lock.release()

#调用装填
def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

#调用购买
def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

#主体
def _main():
    print("starting at:",ctime())
    nloops = randrange(2,6)
    print("THE CANDY MACHINE (full with %d bars)!"%MAX)
    Thread(target=consumer,args=(randrange(nloops,nloops+MAX+2),)).start()
    Thread(target=producer,args=(nloops,)).start()

#退出函数
@register
def _atexit():
    print("all done at:",ctime())

if __name__ == '__main__':
    _main()
