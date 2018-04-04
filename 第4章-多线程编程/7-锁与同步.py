#使用锁来实现同步，保证临界区同一时刻只有一个线程可以访问
#使用2to3工具转换书中代码，已通过运行测试

from atexit import register
from random import randrange
from threading import Thread,Lock,current_thread
from time import sleep,ctime

class CleanOutputSet(set):
    def __set__(self):
        return ",".join(x for x in self)

lock = Lock()
loops = (randrange(2,5) for x in range(randrange(3,7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = current_thread().name
    lock.acquire()
    remaining.add(myname)
    print(("[{}] Started {}".format(ctime(),myname)))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print(("[{}] Completed {} ({} secs)".format(ctime(),myname,nsec)))
    print(("    (remaining:{})".format(remaining or "NONE")))
    lock.release()

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print(("All DONE at:{}".format(ctime())))

if __name__ == '__main__':
    _main()
