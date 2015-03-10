'''
Created on 2015年3月10日

@author: zhiqian.wang
'''
# -*- coding: UTF-8 -*-
#!/usr/bin/python
import smtplib
import urllib

import datetime
from email.mime.text import MIMEText


mailto_list = ["test@autonavi.com"]
mail_host = "mail.autonavi.com"
mail_user = 'test@autonavi.com'
mail_pass = 'password'

def get_time(interval=1):

        now = (datetime.datetime.now()-datetime.timedelta(days = interval)).strftime("%Y-%m-%d")
        return now

def send_mail(to_list,sub,content):
        me = "me" + "<" + mail_user + ">"
        msg = MIMEText(content,_subtype='html',_charset='utf-8')
        msg['Subject'] = sub
        msg['From']    = me
        msg['To']      = ";".join(to_list)

        try:
                s = smtplib.SMTP()
                s.connect(mail_host)
                s.login(mail_user,mail_pass)
                s.sendmail(me,to_list,msg.as_string())
                s.close()
                return True
        except Exception, e:
                print str(e)
                return False

if __name__ == '__main__':

        #url = "file:///home/laughing/work/monitor/s.html"
        #url = "file:///home/laughing/work/monitor-autonavi/s.html"
        url = "file:///root/monitor/result.html"
        sub = "业务报警统计(" + get_time() + ")"


        if send_mail(mailto_list,sub,urllib.urlopen(url).read()):
                print "success"
        else:
                print "error"   
