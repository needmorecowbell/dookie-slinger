#!/usr/bin/python3

import smtplib

sender_email = 'amusciano@gmail.com' # insert user email
sender_name= 'Adam Musciano'
receivers = ['lightlytoasted33@gmail.com'] #insert company email

header = """
From: From {var[sender_name]} <{var[sender_email]} >
To: To {var[receiver_name]} <{var[receiver_email]}>
Subject: {var[subject]}

"""

with open('./res/templates/email.txt', 'r') as myfile:
        body = myfile.read()



message= header+body


for receiver in receivers:
    custom_info = {
            "sender_name":"Adam Musciano",
            "sender_email":sender_email,
            "receiver_name":'BossMan',
            "receiver_email":receiver,
            "company":"Rain Reality",
            "job_title":"web developer",
            "name":"Adam Musciano",
            "subject":"Job Interest"
            }

    #insert templated text, replacing tags with config/contact info

    print(message.format(var=custom_info))

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
        #smtpObj.sendmail(sender, receivers, template.render(Context(custom_info )))         
       # print("Full Message:\n"+ template.render(Context(custom_info)) )
        print( "Successfully sent email")
    except SMTPException:
        print( "Error: unable to send email")



