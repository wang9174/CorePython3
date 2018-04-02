#学习并使用thread模块中的锁

#已通过Python3运行测试（Python3.5.2）
import _thread
from time import sleep, ctime

#将常量独立出来
loops = [4,2]

#使用唯一的loop函数，通过传递不同的参数实现不同的循环
def loop(nloop,nsec,lock):
    print("start loop",nloop,"at:",ctime())
    sleep(nsec)
    print("loop",nloop,"done at:",ctime())
    lock.release()

#创建锁对象，派生线程并分配锁对象，监控锁状态
def main():
    print("starting at:",ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():pass
    print("All done at:",ctime())

if __name__ == '__main__':
    main()
