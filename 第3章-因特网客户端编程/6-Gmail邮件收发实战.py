#使用Gmail完成收发邮件，并包含python版本检查、加密连接、等功能
#编写时处在无网络环境，该脚本未经过运行测试
#在编写中发现有的模块的函数名称可能发生了变化，因此可能导致一些错误，需要后面进行测试

#Python3中没有cStringIO，而是直接从io中导入，可采用下面的方式实现2和3的兼容
try:
    from io import StringIO
except ImportError:
    from cStringIO import StringIO

from imaplib import IMAP4_SSL
from platform import python_version
from poplib import POP3_SSL

#同样，SMTP_SSL在Python2.6版本添加，在2.6.3版本稳定，可采用下面的方式实现兼容
from smtplib import SMTP
release = python_version()
if release >'2.6.3':
    from smtplib import SMTP_SSL
else:
    SMTP_SSL = None

#将用户名密码明文保存是不合理的，因此这里假设有一个secret.pyc字节码文件，
# 用户名和密码是其中的私有信息,通过MAILBOX和PASSWD属性调用
from secret import *
#看到这里我突然想起来，前面遇到的有些参数丢失难道也是这种情况？不不不，肯定是bug

#一些预设参数
who = '{}@gmail.com'.format(MAILBOX)
from_ = who  # from为系统关键字，使用from为变量将导致from关键字失效
to = [who]

headers = ['From:{}'.format(from_),
           'To:{}'.format(','.join(to)),
           'Subject:test SMTP send via 587/TLS',
           ]
body = ['Hello',
        'World',
        ]  #请听题：'world'后面的逗号有什么作用，是否可以去除，添加逗号的原因是什么

msg = '\r\n\r\n'.join(('\r\n'.join(headers),'\r\n'.join(body))) #合并全文，并使用正确的操作符

def getSubject(msg,default = '(NO subject line)'):
    '''
    getSubject(msg)-寻找并返回msg中的subject行，如果没找到返回default
    '''
    for line in msg:
        if line.startwith('Subject:'):
            return line.rstrip()
        if not line:
            return default

#SMTP/TLS 通过TLS连接服务器，发送邮件
print('QAQ***Doing SMTP send via TLS...')
s = SMTP('smtp.gmail.com',587)
if release <'2.6':
    s.ehlo()
s.starttls()
if release <'2.5':
    s.ehlo()
s.login(MAILBOX,PASSWD)
s.sendmail(from_,to,msg)
s.quit()
print("  TLS mail send!")

#POP 下载邮件
print('QAQ***Doing POP recv...')
s = POP3_SSL('pop.gmail.com',995)
s.user(MAILBOX)
s.pass_(PASSWD)
rv, msg, sz =s.retr(s.stat()[0])
s.quit()
line = getSubject(msg)
print('  Received msg via POP:%r'%line)

body = body.replace('587/TLS','465/SSL')

#SMTP/SSL 通过SSL连接服务器，发送邮件
if SMTP_SSL:
    print('QAQ***Doing SMTP send via SSL...')
    s = SMTP_SSL('smtp.gmail.com',465)
    s.login(MAILBOX,PASSWD)
    s.sendmail(from_.to.msg)
    s.quit()
    print('  SSL mail send!')

#IMAP
print('QAQ***Doing IMAP recv...')
s = IMAP4_SSL('imap.gmail.com',993)
s.login(MAILBOX,PASSWD)
rsp,msgs = s.select('INBOX',True)
rsp,data = s.fetch(msgs[0],'(RFC822)')
line = getSubject(StringIO(data[0][1]))
s.close()
s.logout()
print('  Received msg via IMAP:%r'%line)
