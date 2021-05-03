from django.shortcuts import render

from django.http import HttpResponse
import qrcode
from django.utils.six import BytesIO


def index(request):
    return render(request, "index.html")


def generate_qrcode(request):                           # �������ɶ�ά��
    img = qrcode.make('https://www.baidu.com/')         # ����ָ��Ϊ�ٶȵĶ�ά��
    # img = qrcode.make(data)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    response = HttpResponse(image_stream, content_type="image/png")
    return response


def login(request):                                     # ��¼ �� ע��
    datalist = []
    if request.method == "GET":                         # ������ post �� get ������ע�����¼
        name = request.GET.get("name", None)
        password = request.GET.get("pass", None)
        with open("login.txt", "r") as f:
            for line in f:                              # �� f �е�ÿһ�У�ѭ��
                linedata = line.split('--')             # �� -- �ָ���ȡ��ÿ�����ݣ����� linedata=['lk','1234','\n']
                if linedata[0] == name and linedata[1] == password:
                    d = {"name": name, "status": "succeed login!"}
                    datalist.append(d)
                    pp = 1                              # һ���ҵ�ƥ��� �˺�,���� , ���˳� forѭ��
                    break
                else:
                    pp = 0
            if pp == 0:                                 # ��δ�ҵ�,��pp��ֵʼ��Ϊ0
                d = {"name": name, "status": "filed login, maybe your account or password is wrong!"}
                datalist.append(d)
    if request.method == "POST":
        name = request.POST.get("name", None)
        password = request.POST.get("pass", None)
        with open("login.txt", "a+", encoding="utf-8") as f:     # ע������ָ�����뷽ʽΪ utf-8 ������������login.txt��д������
            f.write("{}--{}--\n".format(name, password))         # ע������������� -- ���������ڷ���password�����Ļ��з� \n

    return render(request, "login.html", {"data": datalist})
