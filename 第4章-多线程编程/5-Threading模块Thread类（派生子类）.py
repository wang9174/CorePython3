#先将thread子类化而不是对其直接实例化
#已通过Python3运行测试（Python3.5.2）
import threading
from time import sleep,ctime

loops = [4,2]

#MyThread
class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def getResult(self):
        return self.res
    def run(self):
        #print("starting",self.name,"at:",ctime())
        self.res = self.func(*self.args)
        #print(self.name,"finished at:",ctime())
#loop
def loop(nloop,nsec,):
    print("start loop",nloop,"at:",ctime())
    sleep(nsec)
    print("loop",nloop,"done at:",ctime())

#实例化MyThread，得到返回的实例，然后执行并等待线程结束
def main():
    print("starting at:",ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    #在threading模块中即使不适用join也可以，只有在你需要主线程等待该线程完成等情况下才有必要
    for i in nloops:
        threads[i].join()

    print("All done at:",ctime())

if __name__ == '__main__':
    main()
