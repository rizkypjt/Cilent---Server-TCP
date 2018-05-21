import smtplib

sender = 'kamu8467@gmail.com'
receivers = ['rizkyhidayatpanjaitan97@gmail.com']

message = """From: From rizky <rizkyhidayatpanjaitan03@gmail.com>
TO : Panjaitan <rizkyhidayatpanjaitan97@gmail.com>
Subject: SMTP e-mail test
Insyaa Allah Jadi Ahlul Quran
"""
# try:
username = 'kamu8467@gmail.com'
password = 'Kamu12345'
smtObj = smtplib.SMTP('smtp.gmail.com', 587)
smtObj.ehlo()
smtObj.starttls()
smtObj.login(username,password)
smtObj.sendmail(sender, receivers, message)
smtObj.close()
print "Successfully sent email"
    
# except SMTPException:
#     print "Error: unable to send email"
