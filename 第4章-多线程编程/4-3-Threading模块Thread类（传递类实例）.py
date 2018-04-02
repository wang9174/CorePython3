#传递一个可调用的类（实例）而不仅仅是一个函数
#已通过Python3运行测试（Python3.5.2）

import threading
from time import sleep,ctime

loops = [4,2]

class ThreadFunc(object):
    #构造函数__init__将在实例化时调用，用于设定参数
    def __init__(self,func,args,name=""):
        self.name = name
        self.func = func
        self.args = args
    #当创建新线程时将调用ThreadFunc对象，此时会调用__call__()这个特殊方法
    def __call__(self):
        self.func(*self.args)

# loop函数
def loop(nloop,nsec,):
    print("start loop",nloop,"at:",ctime())
    sleep(nsec)
    print("loop",nloop,"done at:",ctime())

#实例化thread对象时，同时实例化可调用类，然后执行并等待线程结束
def main():
    print("starting at:",ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    #在threading模块中即使不适用join也可以，只有在你需要主线程等待该线程完成等情况下才有必要
    for i in nloops:
        threads[i].join()

    print("All done at:",ctime())

if __name__ == '__main__':
    main()
