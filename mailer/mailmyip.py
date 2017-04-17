import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import netifaces as ni

# Change to your own account information
to = ''
gmail_user = ''
gmail_password = ''
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()

eth0Ip = ni.ifaddresses('eth0')
wlan0Ip = ni.ifaddresses('wlan0')

my_ip = 'Your eth0 IP is '+str(eth0Ip)+', wlan0 is '+str(wlan0Ip)
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
