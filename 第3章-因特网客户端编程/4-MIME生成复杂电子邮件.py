#使用MIME（邮件互换消息拓展）模块，创建并发送带有附件的及格式的电子邮件
#编写时处在无网络环境，该脚本未经过运行测试

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

SENDER = "发送人邮箱"
RECIPS = "收件人邮箱"
IMG_FILE = "图片地址"

#多部分选择消息：文本与HTML
#由客户端来选择显示text版或HTML版
def make_mpa_msg():
    email = MIMEMultipart('alternative')  #如果不传递这个参数，则文本和html会分别作为消息附件
    text = MIMEText('Hello World!\r\n',"plain")
    email.attach(text)
    html = MIMEText('<html><body><h4>Hello World!</h4>''</body></html>','html')
    email.attach(html)
    return email

#生成一个MIMEimage实例，添加一个头后返回给用户
def make_img_msg(fn):
    f= open(fn,'r')
    data = f.read()
    f.close()
    email = MIMEImage(data,name=fn)
    email.add_header('Content-Disposition','attachment;filename="{}"'.format(fn))
    return email

#湖区发件人、收件人、消息正文，然后传送消息
def sendMsg(fr,to,msg):
    s = SMTP('localhost')
    errs = s.sendemail(fr,to,msg)
    s.quit()

#调用函数创建消息，添加From、To、Subject字段，发送
if __name__ == '__main__':
    print('Sending multipart alternative msg...')
    msg = make_mpa_msg()
    msg['from'] = SENDER
    msg['To'] = ','.join(RECIPS)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(SENDER,RECIPS,msg.as_string())

    print('Sending image msg...')
    msg = make_img_msg(IMG_FILE)
    msg['from'] = SENDER
    msg['To'] = ','.join(RECIPS)
    msg['Subject'] = 'image file test'
    sendMsg(SENDER,RECIPS,msg.as_string())
