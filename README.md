# monitor-notify

You should install the mako library first before you gernerate html. You can use pip command.
pip install mako

1 python getemail.py 
Receive the yesterday's email , then write the contents into the  file named monitor-2015-03-09.csv。 

2 python do.py > result.html 
Generate the html from the csv file.

3 python sendemail.py 
send the html to sb.



do.py 
Set the subject or summary of the email.

anylyze.py
You can add your search char here.

sendmail.py
url = "file:///root/monitor/result.html"
