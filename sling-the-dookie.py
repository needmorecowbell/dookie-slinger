#!/usr/bin/python3

import smtplib


sender_email = 'from@gmail.com' # insert user email
sender_name= 'Adam Musciano'
receivers = ['to@todomain.com'] #insert company email

message = """From: From ${sender_name} <${sender_email}>
To: To ${receiver_name} <${receiver_email}>
Subject: ${subject}

${body}
"""

#insert templated text, replacing tags with config/contact info

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com',587)
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
