#使用SMTP和POP3创建一个既能发送又能接受邮件的客户端
#编写时处在无网络环境，该脚本未经过运行测试
#自行测试时需要修改服务器名称和电子邮件地址
from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPsvr = 'smtp.python.is.good'
POP3svr = 'pop.python.is.good'

who = 'starseeker@python.is.good'
# RFC2822要求消息头与正文用空行分开
body = '''
From:{0}s
To:{0}s
Subject:test msg

Hello World!
'''.format(who)

#发送邮件
sendSvr = SMTP(SMTPsvr)
#第三个参数origMsg是电子邮件消息本身，但这个参数并未出现过，我觉得是编辑又乱来了
errs = sendSvr.sendmail(who,[who],origMsg)
sendSvr.quit()
#断言，若errs长度等于0则抛出异常，逗号后面为抛出异常时附带的异常提示（AssertionError）
assert len(errs)==0, errs
sleep(10)

#下载邮件并判断发送与接受的内容是否一致
recvSvr = POP3(POP3svr)
recvSvr.user('starseeker')
recvSvr.pass_('supriseMotherFucker')
# stat()得到可用消息列表，retr()下载消息
rsp,msg,siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep+1:]
#又一个石头里冒出来的参数，emmm，也没办法测试，就先扔这
assert origbody == recvBody
