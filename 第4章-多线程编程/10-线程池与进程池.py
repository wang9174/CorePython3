#使用线程池（进程池）向亚马逊请求查询图书排名
#经运行测试,第三个查询正常，前两个失败报错（手动访问页面正常）,错误原因待定
from atexit import register
from re import compile
from time import ctime
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from urllib.request import urlopen as uopen

REGEX = compile(b"#[\d,]+ in Books ")
AMZN = "http://amazon.com/dp/"
ISBNs = {
    "0132269937":"Core Python Programming",
    "0132356139":"Python Web Development with Django",
    "0137143419":"Python Fundamentals",
}

#拼接链接、读取页面、返回正则匹配
def getRanking(isbn):
    page = uopen("{}{}".format(AMZN,isbn))
    data = page.read()
    page.close()
    return str(REGEX.findall(data)[0],"utf-8")

#单下划线代表只能被本模块的代码使用，而不能导出到外部使用
def _showRanking(isbn):
    print("-{} ranked {}".format(ISBNs[isbn],getRanking(isbn)))

def _main():
    print("At",ctime(),"on Amazon...")
    with ThreadPoolExecutor(3) as excutor:
        for isbn in ISBNs:
            excutor.submit(_showRanking, isbn)


#注册一个退出函数，脚本退出之前会调用这个函数
@register
def _atexit():
    print("all DONE at:",ctime())

if __name__ == '__main__':
    _main()
