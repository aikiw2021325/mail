#!python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import random
import math
import smtplib
import ssl
from email.mime.text import MIMEText


def SendGmail(ToAddress, val1, val2):
    gmail_account = "aiki.w1817137@gmail.com"
    gmail_password = "aiki0710"

    subject = "test mail"
    body = "あなた:"+val1+"相手:"+val2

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["To"] = ToAddress
    msg["From"] = gmail_account

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg)
    server.close()
    

cgitb.enable()
form = cgi.FieldStorage() # cgiオブジェクト作成
v1 = form.getfirst('value1') # nameがvalue1の値を取得
v2 = form.getfirst('value2') # nameがvalue2の値を取得

ran = random.random()*100
ran = math.floor(ran)
ran = str(ran)

# ブラウザに戻すHTMLのデータ
print("Content-Type: text/html")
print()

print(str(v1)+"と")
print(str(v2)+"の相性は\n")

print(ran+"%です")

#SendGmail("aiki.w1817137@gmail.com", str(v1), str(v2))
SendGmail("piropiro827@icloud.com", str(v1), str(v2))


