# /busr/bin/env python

import psutil
import datetime
import yagmail


def monitoring(time):
    now = datetime.datetime.now().strftime("%Y-%m%d %H:%M:%S")
    host_info = psutil.net_if_addrs()['ens33'][0][1]

    cpu_per = psutil.cpu_percent(interval=time)
    cpu_total = psutil.cpu_count()

    mem_info = psutil.virtual_memory().percent
    mem_total = psutil.virtual_memory().total / 1024 / 1024 / 1024

    disk_total = psutil.disk_usage('/').total / 1024 / 1024 / 1024
    disk_info = psutil.disk_usage('/').percent

    net_recv = psutil.net_io_counters().bytes_recv
    net_sent = psutil.net_io_counters().bytes_sent
    net_addr = psutil.net_if_addrs()['ens33'][0][1]

    log_str = "|----------------------|---------------|------------------|-----------------|------------------| ".ljust(
        100) + '\n'
    log_str += "|      监控时间        |  CPU 使用率   |  Memory 使用率   |  / 分区使用率   |    网络收发量    |".ljust(100) + '\n'
    log_str += "| 主机：%s   |  (总共 %d 核)  | (总计%d G内存)    | (共计 %d G硬盘) |                  |".ljust(100) % (
    net_addr, cpu_total, mem_total, disk_total,) + '\n'
    log_str += "|----------------------|---------------|------------------|-----------------|------------------|".ljust(
        100) + '\n'
    log_str += "|  %s  |   %s %%       |   %s %%         |     %0.4s %%      | 收：%0.4s/发：%0.4s|" % (
    now, cpu_per, mem_info, disk_total, net_recv, net_sent) + '\n'
    log_str += "|----------------------|---------------|------------------|-----------------|------------------|".ljust(
        50) + '\n'
    #     print(log_str)

    with open('sysinfo.txt', 'a+') as f:
        f.write(log_str)
def send_mail():
    ya_obj = yagmail.SMTP(user="13691435845@163.com", password='xxxxx1', host='smtp.163.com')
    ya_obj.send('1071102039@qq.com', '【系统监控报告】', log_str)


def main():
    '''程序入口'''
    while True:
        monitoring(5)
        if cpu_per > 3 or disk_info > 80:
            send_mail()


if __name__ == '__main__':
    main()
