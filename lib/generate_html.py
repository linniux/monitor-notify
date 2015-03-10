'''
Created on 2015年3月10日

@author: zhiqian.wang
'''

from mako.template import Template
from mako import exceptions

import datetime
import sys
reload(sys)
#sys.setdefaultencoding( "utf-8" )


def get_time(interval=1):

        now = (datetime.datetime.now()-datetime.timedelta(days = interval)).strftime("%Y-%m-%d")
        return now


try:
        t = Template(filename='templates/monitor.html',module_directory='./')
        print t.render(time=get_time(),title="报警结果统计",summary="问题记录",detail="自动恢复，，故障，，，")
        
except:
        print exceptions.text_error_template().render()