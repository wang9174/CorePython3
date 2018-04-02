#使用比thread模块更好的threading模块，通过实例化Thread类并传递给它一个函数，实现创建线程
#已通过Python3运行测试（Python3.5.2）
import threading
from time import sleep,ctime

loops = [4,2]

#
def loop(nloop,nsec,):
    print("start loop",nloop,"at:",ctime())
    sleep(nsec)
    print("loop",nloop,"done at:",ctime())

#实例化thread对象时，将函数与参数传递进去，得到返回的thread实例，然后执行并等待线程结束
def main():
    print("starting at:",ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    #在threading模块中即使不适用join也可以，只有在你需要主线程等待该线程完成等情况下才有必要
    for i in nloops:
        threads[i].join()

    print("All done at:",ctime())

if __name__ == '__main__':
    main()
