import time
import yagmail
import threading

def sendmail():
    ya_obj = yagmail.SMTP (user="13691435845@163.com", password='xxxx1', host='smtp.163.com')
    ya_obj.send('1071102039@qq.com','日志-ERROR-告警',x)

def tailf(path):
    offset = 0
    event = threading.Event()
    try:
        while not event.is_set():
            with open(path) as f:
                if offset > f.tell():
                    offset = 0
                f.seek(offset)
    #             for line in f:
    #                 yield line
                yield from f
                offset = f.tell()
    #         time.sleep(1)
            event.wait(1) # 优雅退出
    except KeyboardInterrupt:
        event.set()

for x in tailf('sysinfo.txt'):
    print(x)
    if 'error' in x:
        sendmail()
