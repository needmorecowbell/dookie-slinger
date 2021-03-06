#!/usr/bin/python3

import smtplib
import json
import progressbar

with open('./res/config.json', 'r') as myfile:
    config = json.loads(myfile.read())

with open('./res/contacts/contacts.json','r') as myfile:
    receivers = json.loads(myfile.read()) # call by using receivers['group']['item']
 
with open('./res/templates/email.txt', 'r') as myfile:
        body = myfile.read()


#standard smtp protocol header template
header = """From: From {var[sender_name]} <{var[sender_email]} >
To: To {var[receiver_name]} <{var[receiver_email]}>
Subject: {var[subject]}

"""

message= header+body 

#Setup mail
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(config['sender_email'], config['sender_password']) 

widgets = [
        'Completed:', progressbar.Percentage(),
        'ETA: ', progressbar.ETA()
        ]

bar = progressbar.ProgressBar(widgets= widgets, max_value= len(receivers['companies']))
progressCount=0

for receiver in receivers['companies']: 
    custom_info = {
            "receiver_name":receiver['name'],
            "receiver_email":receiver['email'],
            "company":receiver['company'],
            "job":receiver['job'],
            "subject":receiver['subject']
            } #Adds all additional variables that might be in template
    #add new key/val pairs to this dictionary for valid variables in formatting
 
    data = config.copy()
    data.update(custom_info) #append custom_info to final dictionary


    try:
        
        print("Full Message:\n"+message )
        smtpObj.sendmail(config['sender_email'], receiver['email'], message.format(var=data))
        
        print( "\nSuccessfully sent email\n")

        progressCount+=1
        bar.update(progressCount)

        print("\n**************************\n\n")

    except SMTPException:
        print( "Error: unable to send email")


print("The dookies have all been slung!")
bar.finish()

