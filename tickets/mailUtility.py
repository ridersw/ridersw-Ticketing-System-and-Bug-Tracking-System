import pandas as pd
import smtplib
#from email.message import EmailMessage
import time
import sys

#try:
#    from email.message import EmailMessage
#except:
#    print('The message txt not found')
#    print('Please create message.txt and store your message as "messages" ')         



def getUpdate(ticket_ID, title, assigned_engineer, engineer_email, user_name):
    #ticket_id, ticket_title, assigned_engineer, engineer_email, assigned_engineer, user_name

    password = "LondonParis#1"

    fromEmail = "ticketingtoolDjango@gmail.com"

    messages = f"""Greetings {assigned_engineer},

    {user_name} has requested an update on {ticket_ID}: {title}. Please use the below URL to provide an update.

    This is an automated email. Please do not reply to this email as this mailbox is not monitored.

    Best,
    Bee, Ticketing Tool """


    msg = EmailMessage()

    msg.set_content(messages)

    msg['Subject'] = '[Ticketing Tool] Requested Update on ' + ticket_ID
    msg['From'] = fromEmail

    msg['To'] = engineer_email
     
    try: 
        print('Trying to send mail')            
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(fromEmail, password)
        print('Server Login Successfully')
        server.send_message(msg)
        print(f"email sent successfully")
        server.quit()
        return True
    except: 	
        print('Error Occurred in Server Login')
        print(f'Error Sending Email to {emails}')
        sys.exit()
        return False  