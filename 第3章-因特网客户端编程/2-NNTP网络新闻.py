#连接NNTP，下载并显示Python新闻组里的最新文章的前二十有数据的行
#编写时处在无网络环境，该脚本未经过运行测试
import nntplib
import socket

HOST = 'your.nntp.server'
GRNM = 'comp.lang.python'
#USER = 'OldDriver'
#PASS = 'youllNeverGuess'

def main():
    try:
        n = nntplib.NNTP(HOST) #如果有用户名与密码，可以填入
    except socket.gaierror as e:
        print('ERROR: cannot reach host "{}"'.format(HOST))
        print('  ("{}")'.format(eval(str(e))[1]))
        return
    except nntplib.NNTPPermanentError as e:
        print('ERROR: access denied on "{}"'.format(HOST))
        print('服务器拒绝了我QAQ！哼╭(╯^╰)╮')
        print('  ("{}")'.format(str(e)))
        return
    print('QAQ__Connected to host "{}"'.format(HOST))

    try:
        #获取服务器响应、文章数量、第一个文章编号、最后一个文章编号、组名
        rsp,ct,fst,lst,grp = n.group(GRNM)
    except nntplib.NNTPPermanentError as e:
        print('ERROR: cannot load group "{}"'.format(GRNM))
        print('嘤嘤嘤，加载不进去QAQ')
        print('  ("{}")'.format(str(e)))
        print('服务器说这是开往幼儿园的车，你需要身份认证~')
        print("滴，学生卡~")
        n.quit()
        return
    except nntplib.NNTPTemporaryError as ee:
        print('ERROR: group "{}" unavailable'.format(GRNM))
        print('  ("{}")'.format(str(e)))
        n.quit()
        return
    print('QAQ__我找到{}这个组啦~'.format(GRNM))

    rng = "{}-{}".format(lst,lst)
    # xhdr返回rng范围（从lst到lst）的文章内，带有消息头关键字“from”的列表 (response, list)
    #其中list是内含（id，text）元组的列表，id是文章编号，text是所请求的标题对应的文本
    rsp,frm = n.xhdr('from',rng)
    rsp,sub = n.xhdr('subject',rng)
    rsp,dat = n.xhdr('date',rng)
    print(''''QAQ__Found last article (#{}):
    
    From:{}
    Subject:{}
    Date:{}
    '''.format(lst,frm[0][1],sub[0][1],dat[0][1]))

    #根据ID获取文章正文
    rsp, anum, mid, data = n.body(lst)
    displayFirst20(data)
    n.quit()

def displayFirst20(data):
    # rstrip() 删除 string 字符串末尾的指定字符（默认为空格）
    #continue 语句跳出本次循环，而break跳出整个循环
    print('QAQ__前二十行非空文本：')
    count = 0  #设置计数器
    lines = (line.rstrip() for line in data)  #移除末尾空格，方便判断空行
    lastBlank = True
    for line in lines:
        if line:
            lower = line.lower()
            if lower.startwith('>') and not lower.startwith('>>>') \
                or lower.startwith('|') or lower.startwith("in article") \
                or lower.endwith('writes:') or lower.endwith("wrote:"):
                continue
        #如果上一行已经是空行，那么下一行不能是空行
        if not lastBlank or line:
            print('  {}'.format(line))
            if line:
                count +=1
                lastBlank = False
            else:
                lastBlank = True
        if count == 20:
            break
if __name__ == '__main__':
    main()

