# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = '3431780376@qq.com'
receiver = ['3431780376@qq.com', 'lk_lijia0606@163.com']    # 接收人列表

smtpserver = 'smtp.qq.com'

sender = '3431780376@qq.com'                                # 发件人邮箱账号
password = 'anwepswaphydcjab'                               # 发件人密码（这里是，QQ邮箱授权码）
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'this is a test message'               # 标题

# 构造附件1
att1 = MIMEText(open('C:\\Users\\PC\\test1.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test11.txt"'
msgRoot.attach(att1)

# 构造附件2
att2 = MIMEText(open('C:\\Users\\PC\\1.jpg', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="1.jpg"'
msgRoot.attach(att2)

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(sender, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
