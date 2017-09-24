#!/usr/bin/python3

import smtplib
import json

with open('./res/config.json', 'r') as myfile:
    config = json.loads(myfile.read())

with open('./res/contacts/contacts.json') as myfile:
    receivers = json.loads(myfile.read())
    

header = """From: From {var[sender_name]} <{var[sender_email]} >
To: To {var[receiver_name]} <{var[receiver_email]}>
Subject: {var[subject]}

"""

with open('./res/templates/email.txt', 'r') as myfile:
        body = myfile.read()


message= header+body

for receiver in receivers['companies']:
    custom_info = {
            "receiver_name":receiver['name'],
            "receiver_email":receiver['email'],
            "company":receiver['company'],
            "job":receiver['job'],
            "subject":receiver['subject']
            }
    data = config.copy()
    data.update(custom_info) #append both dictionaries to data



    #insert templated text, replacing tags with config/contact info
    print(message.format(var=data))

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
        #smtpObj.sendmail(sender, receivers, template.render(Context(custom_info )))         
       # print("Full Message:\n"+ template.render(Context(custom_info)) )
        print( "Successfully sent email")
    except SMTPException:
        print( "Error: unable to send email")



