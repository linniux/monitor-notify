'''
Created on 2015年3月10日

@author: 
'''


import re



class Parsefile(object):
        ''' Some ,,,,'''
        def __init__(self,monitorfile):
                self.monitorfile = monitorfile
                self.detail = re.compile(r'test|Test|Film|QQ|Google',re.I|re.M|re.S)
                self.summary = re.compile(r'故障报警|故障恢复')
                self.time = re.compile(r'2015 00|2015 01|2015 02|2015 03|2015 04|2015 05|2015 06|2015 07|2015 08|2015 09|2015 10|2015 11|2015 12|2015 13|2015 14|2015 15|2015 16|2015 17|2015 18|2015 19|2015 20|2015 21|2015 22|2015 23|2015 24')
                self.f = open(self.monitorfile,"r")

        def __del__(self):
                self.f.close()

        def counts(self):
                darr = {}
                sarr = {}
                tarr = {}
                lines = self.f.readlines()
                for line in lines:
                        dmatch = self.detail.search(line)
                        smatch = self.summary.search(line)
                        tmatch = self.time.search(line)

                        if dmatch:
                                if(darr.has_key(dmatch.group(0))):
                                        darr[dmatch.group(0)] += 1
                                else:
                                        darr.setdefault(dmatch.group(0),1)
                        if smatch:
                                if(sarr.has_key(smatch.group(0))):
                                        sarr[smatch.group(0)] += 1
                                else:
                                        sarr.setdefault(smatch.group(0),1)
                        if tmatch:
                                if(tarr.has_key(tmatch.group(0))):
                                        tarr[tmatch.group(0)] += 1
                                else:
                                        tarr.setdefault(tmatch.group(0),1)
                return darr,sarr,tarr
