from django.shortcuts import render

from django.http import HttpResponse
import qrcode
from django.utils.six import BytesIO


def index(request):
    return render(request, "index.html")


def generate_qrcode(request):                           # 在线生成二维码
    img = qrcode.make('https://www.baidu.com/')         # 这里指定为百度的二维码
    # img = qrcode.make(data)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    response = HttpResponse(image_stream, content_type="image/png")
    return response


def login(request):                                     # 登录 与 注册
    datalist = []
    if request.method == "GET":                         # 这里用 post 与 get 来区分注册与登录
        name = request.GET.get("name", None)
        password = request.GET.get("pass", None)
        with open("login.txt", "r") as f:
            for line in f:                              # 对 f 中的每一行，循环
                linedata = line.split('--')             # 以 -- 分隔读取的每行数据，例如 linedata=['lk','1234','\n']
                if linedata[0] == name and linedata[1] == password:
                    d = {"name": name, "status": "succeed login!"}
                    datalist.append(d)
                    pp = 1                              # 一旦找到匹配的 账号,密码 , 则退出 for循环
                    break
                else:
                    pp = 0
            if pp == 0:                                 # 若未找到,则pp的值始终为0
                d = {"name": name, "status": "filed login, maybe your account or password is wrong!"}
                datalist.append(d)
    if request.method == "POST":
        name = request.POST.get("name", None)
        password = request.POST.get("pass", None)
        with open("login.txt", "a+", encoding="utf-8") as f:     # 注意这里指定编码方式为 utf-8 ，这样可以在login.txt中写入中文
            f.write("{}--{}--\n".format(name, password))         # 注意这里采用两次 -- ，这样用于分离password与后面的换行符 \n

    return render(request, "login.html", {"data": datalist})
