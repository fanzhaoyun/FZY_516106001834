import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.163.com'
# 发送邮箱用户/密码
user = 'fanzhaoyun728@163.com'
password = '728111fzy'
# 发送邮箱
sender = 'fanzhaoyun728@163.com'
# 接收邮箱
receiver = '1207322958@qq.com'
# 发送邮件主题
subject = '范照云测试报告（自动发送）'

# 发送的附件
sendfile = open('help.txt', 'rb').read()

# 创建一个带附件的实例
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = Header(subject, 'utf-8')                         # 定义邮件标题
# 需要添加这两个赋值
msgRoot['From'] = sender
msgRoot['To'] = receiver

# 邮件正文内容
msgRoot.attach(MIMEText('你好，今天是星期六，天气不错，适合出去玩!', 'plain', 'utf-8'))

# 构造附件
att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="help.txt"'
msgRoot.attach(att)

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()