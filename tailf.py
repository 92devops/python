import time
import yagmail

def sendmail():
    ya_obj = yagmail.SMTP (user="13691435845@163.com", password='xxxxxxxx1', host='smtp.163.com')
    ya_obj.send('1071102039@qq.com','日志告警',x)

def tailf(path):
    offset = 0
    while True:
        with open(path) as f:
            f.seek(offset)
#             for line in f:
#                 yield line
            yield from f
            offset = f.tell()
        time.sleep(1)

for x in tailf('sysinfo.txt'):
    print(x)
    if 'error' in x:
        sendmail()
