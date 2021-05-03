# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '3431780376@qq.com'                                    # 发件人邮箱账号
my_pass = 'anwepswaphydcjab'                                       # 发件人密码（这里是，QQ邮箱授权码）
my_user = 'lk_lijia0606@163.com'                                   # 收件人邮箱账号0
my_user1 = '3431780376@qq.com'                                     # 收件人邮箱账号1


def mail():
    ret = True
    try:
        msg = MIMEText('这里是发送的邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["lk", my_sender])                # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["", my_user])                      # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "Python测试发邮件"                         # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)                        # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)                                     # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, my_user1], msg.as_string())     # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()                                               # 关闭连接
    except Exception:                                               # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
