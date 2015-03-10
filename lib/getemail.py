#!/usr/local/bin/python2.7
# encoding: utf-8
'''
lib.getemail -- shortdesc

lib.getemail is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2015 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import imaplib
import email

import sys
reload(sys)
#sys.setdefaultencoding('utf-8')


import time
import datetime
import csv

NOW = time.strftime('%d-%b-%Y',time.localtime())
TOMORROW = time.strftime('%d-%b-%Y',time.localtime(time.time()+24*60*60))  
YESTERDAY = time.strftime('%d-%b-%Y',time.localtime(time.time()-24*60*60))  
NOW1 = time.strftime('%d-%b-%Y',time.localtime(time.time()-24*60*60))  

MAILTIMECYCLE = '\'(SINCE "%s" BEFORE "%s")\'' % (YESTERDAY,NOW) 
print MAILTIMECYCLE  

INTERVAL = 1


def get_time(interval=INTERVAL):

        now = (datetime.datetime.now()-datetime.timedelta(days = interval)).strftime("%Y-%m-%d")
        return now

def parserHeader(message):


        subject = ""

        try:
                subject = unicode(message.get('subject').encode('utf-8'))
        except:
                subject = unicode(message.get('subject').decode('gb2312'))
        date = unicode(message.get('date').encode('utf-8'))
        mailfrom = unicode(message.get('from').encode('utf-8'))

        mailheader = []
        d,s,m = "","",""

        try:
                sb =  email.Header.decode_header(email.Header.Header(subject))
                dt =  email.Header.decode_header(email.Header.Header(date))
                mf = email.Header.decode_header(email.Header.Header(mailfrom))

                d = unicode(dt[0][0].encode('utf-8'))
                s = unicode(sb[0][0], sb[0][1]).encode('utf-8')


                m = unicode(mf[0][0].encode('utf-8'))




        except:
                s = subject


        mailheader.append((d,s,m))
        return mailheader

def check_email():

        user = "test@alibaba-inc.com" 
        host = "imap.alibaba-inc.com"
        port = 993
        pwd  = ""

        #M is a connected IMAP4 instance
        M = imaplib.IMAP4_SSL(host,port)
        M.login(user,pwd)
        #M.select(readonly=True)
        M.select(readonly=True)
        #print M.list()

        #typ, msgnums = M.search(None, 'FROM', '"zhiqian.wang@autonavi.com"')
        #typ, data = M.search(None,'(SINCE "07-Mar-2015" before "11-Mar-2015")')
        typ, data = M.search(None,eval(MAILTIMECYCLE))
        
        print type(typ)

        l = []

        for num in data[0].split()[::-1]:
                typ , data  = M.fetch(num,'(RFC822)')

                text = data[0][1]
                message = email.message_from_string(text)
                l.append(parserHeader(message))

        M.close()
        M.logout()

        return l




if __name__ == '__main__':
        a = check_email()

        resultfile = 'monitor-' + get_time() + '.csv'
        
    
        with open(resultfile,'a') as csvfile:
                        filednames = ['date','subject','mailfrom']
                        writer = csv.DictWriter(csvfile, filednames)

                        writer.writeheader()
                        try:
                                for b in a:
                                        if b == None:
                                                pass
                                        else:
                                                for i in b:
                                                        writer.writerow({'date': i[0], 'subject': i[1],'mailfrom': i[2]})
                        except TypeError:
                                pass
