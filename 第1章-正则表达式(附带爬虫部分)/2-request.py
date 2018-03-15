import urllib.request
import urllib.parse

url = "http://httpbin.org/post"
headers = {
    "User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Host":"httpbin.org"
}
dict = {
    "hello":"world"
}
data = bytes(urllib.parse.urlencode(dict),encoding="utf-8") #处理为字节流
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST") #构造格式

response = urllib.request.urlopen(req) #调用
print(response.read().decode("utf-8"))
