# -*- coding:utf-8 -*-


import os
import logging
import time
import smtplib
import email.MIMEMultipart
import email.MIMEText
from email.mime.application import MIMEApplication

FILE = os.getcwd()



def WriteLog(logstr,level):
    '日志输出通用函数 等级 1-debug 、2-info 、3-warning 、4-error 、5-critical'
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s]:[%(filename)s] [%(levelname)s] %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=os.path.join(FILE,'runlog.log'),
                        filemode='w'
                         )
    if level == 1:
        logging.debug(logstr)
    elif level == 2:
        logging.info(logstr)
    elif level == 3:
        logging.warning(logstr)
    elif level == 4:
        logging.error(logstr)
    elif level == 5:
        logging.critical(logstr)
    else:
        pass

def SendMail(mailist):
    '邮件发送函数'
    From = "870937931@qq.com"
    ToList = ["1350084249@qq.com", "1932170@qq.com", "1592368145@qq.com", "1073892558@qq.com"]

    server = smtplib.SMTP("smtp.qq.com")
    server.login('870937931', 'zgsboy@888')

    msg = email.MIMEMultipart.MIMEMultipart()

    text_msg = email.MIMEText.MIMEText(u"数据发布日志", _charset="utf-8")

    msg.attach(text_msg)

    msg["Subject"] = u"每日土地统计" + curdate
    msg["From"] = From
    msg["To"] = ";".join(ToList)

    part = MIMEApplication(open(filename, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename='land' + curdate + '.xls')
    msg.attach(part)

    server.sendmail(From, ToList, msg.as_string())

    server.close()
    sendmail()


def BuildReport():
    '''生成报告函数:
       内容:
       开始时间:
       结束时间：
       同步列表：
       同步记录数：150305035行
       同步结果：完成
       同步质量：良好   达标   偏慢
    '''
    pass