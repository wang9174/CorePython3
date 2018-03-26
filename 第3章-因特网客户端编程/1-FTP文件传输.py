#使用FTP在Mozilla网站下载bugzilla代码
#原书中的此段代码及其解释有三处以上错误，就这还是第三版？校对人员统统扣工资
#编写时处在无网络环境，该脚本未经过运行测试
import ftplib
import os
import socket

HOST = "ftp.mozilla.org"
DIRN = "pub/mozilla.org/webtools"
FILE = "bugzilla-LATEST.tar.gz"

#实现带有错误检查的FTP下载程序
def main():
    #创建一个FTP对象并尝试连接到FTP服务器
    try:
        f= ftplib.FTP(HOST)
    except(socket.error,socket.gaierror) as e:
        print('Error: cannot reach "{0}"'.format(HOST))
        return
    print('QAQ__Conected to host "%s"'%HOST)     #两种不同的格式化方法，其中format在2.4版本引进

    #尝试匿名登录
    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('QAQ__logged in as anonymous')

    #跳转到目的目录
    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "{}"'.format(DIRN))
        f.quit()
        return
    print('QAQ__changed to "{}"folder'.format(DIRN))

    #下载文件
    try:
        #向retrbinary函数传递回调函数，用于创建文件的本地版本
        f.retrbinary('RETR {}'.format(FILE),open(FILE,"wb").write())
    except ftplib.error_perm:
        print('ERROR: cannot read file "{}"'.format(FILE))
        os.unlink(FILE)  #如果出错，移除该空文件
    else:
        print('QAQ__Download "{}" to CWD'.format(FILE))
    f.quit()

#使用惯用的独立脚本运行办法
if __name__ == '__main__':
    main()
