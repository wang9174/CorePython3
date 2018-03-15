import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
request = urllib.request.urlopen("https://httpbin.org/post",data=data)
print(request.read().decode("utf-8"))

#data 参数是可选的，如果要添加 data，它要是字节流编码格式的内容，即 bytes 类型，
# 通过 bytes() 方法可以进行转化，另外如果传递了这个 data 参数，它的请求方式就不再是 GET 方式请求，而是 POST。
