#使用email包里面的几个工具解析电子邮件
#编写时处在无网络环境，该脚本未经过运行测试
import email

#
def processMsg(entire_msg):
    body = ''
    msg = email.message_from_string(entire_msg)  #解析消息
    if msg.is_multipart():
        for part in msg.walk():  #遍历附件
            if part.get_content_type() =='text/plain':  #获得MIME类型
                body = part.get_payload()  #获取消息正文的特定部分，客户端获取text、网页获取HTML
                break
            else:
                body = msg.get_payload(decode=True)
    else:
        body = msg.get_payload(decode=True)
    return body
