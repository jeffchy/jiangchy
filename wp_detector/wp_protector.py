from email.mime.text import MIMEText
import urllib.request
# import re
import smtplib

def send():
    msg = MIMEText('hello, check your wp!...by Jeff LOL ', 'plain', 'utf-8')

    from_addr = '924284013@qq.com'
    # password = 'zmenqbemcwqbbeej'
    password='ftequgzpnyjnbeic'
    smtp_server = 'smtp.qq.com'

    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.connect(smtp_server)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,['jiangchy@shanghaitech.edu.cn','nianzhl@shanghaitech.edu.cn','924284013@qq.com'],msg.as_string())
    print('asdfas')
    server.quit()


url = 'http://www.xuyiwenzhuzhuzhu.cn'
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
if len(data) < 1000:
    send()
