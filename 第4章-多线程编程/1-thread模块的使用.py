#初步使用thread模块，了解多线程编程
#在 Python3 中不能再使用”thread” 模块。为了兼容性，Python3 将 thread 重命名为 “_thread”
#已通过Python3运行测试（Python3.5.2）
import  _thread
from time import sleep, ctime

def loop0():
    print('Start loop 0 at:',ctime())
    sleep(4)
    print('loop 0 done at:',ctime())

def loop1():
    print('start loop 1 at:',ctime())
    sleep(2)
    print("loop 1 done at:",ctime())

#并发执行两个循环
def main():
    print('starting at:',ctime())
    _thread.start_new_thread(loop0,())  #必须包含两个参数，及时不需要传参也需要传递一个空元组
    _thread.start_new_thread(loop1,())
    #thread的缺点就是如果不阻止主程序继续执行，它就会不管线程的情况直接执行下去而退出程序
    #因此我们将在下一个例子引入锁的概念
    sleep(6)
    print("All done at:",ctime())

if __name__ == '__main__':
    main()
