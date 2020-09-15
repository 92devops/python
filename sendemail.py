import yagmail

ya_obj = yagmail.SMTP (user="13691435845@163.com", password='xxxxxx1', host='smtp.163.com')

content = '你好， 王哥'

# ya_obj.send('','王哥亲启',content)

ya_obj.send('xxxxx@qq.com','王哥亲启',content)
