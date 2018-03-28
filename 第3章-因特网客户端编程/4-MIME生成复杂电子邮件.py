#使用MIME（邮件互换消息拓展）模块，创建并发送带有附件的及格式的电子邮件
#编写时处在无网络环境，该脚本未经过运行测试

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

#多部分选择消息：文本与HTML
def make_mpa_msg():
    email = MIMEMultipart('alternative')
