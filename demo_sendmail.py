# encoding: utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")     #加载site.py,导致编码格式需要重新
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail():
    # 读取测试报告内容
    with open('report_file.txt', 'r') as f:
        content = f.read().decode('utf-8')

    msg = MIMEMultipart('mixed')
    # 添加邮件内容
    msg_html = MIMEText(content, 'html', 'utf-8')
    msg.attach(msg_html)

    # 添加附件
    msg_attachment = MIMEText(content, 'html', 'utf-8')
    msg_attachment["Content-Disposition"] = 'attachment; filename="{0}"'.format('report_file.txt')
    msg.attach(msg_attachment)

    msg['Subject'] = mail_subjet
    msg['From'] = mail_user
    msg['To'] = ';'.join(mail_to)
    try:
        # 连接邮件服务器
        s = smtplib.SMTP(mail_host, 25)
        # 登陆
        s.login(mail_user, mail_pwd)
        # 发送邮件
        s.sendmail(mail_user, mail_to, msg.as_string())
        # 退出
        s.quit()
    except Exception as e:
        print "Exceptioin ", e

if __name__ == '__main__':
    # 邮件服务器
    mail_host = 'smtp.163.com'
    # 发件人地址
    mail_user = 'noranet@163.com'
    # 发件人密码
    mail_pwd = '123456w'
    # 邮件标题
    mail_subjet = u'NoseTests_测试报告'
    # 收件人地址list
    mail_to = ['norawill@126.com','wll_hz@163.com']
    # 测试报告名称
    report_file = 'TestReport.html'

    # 单独写文件，生成测试报告
    h = open('report_file.txt', 'w')
    h.write('Hello, world!')
    h.close()

    # 发送测试报告邮件
    print 'Send Test Report Mail Now...'
    send_mail()
    print 'over......'