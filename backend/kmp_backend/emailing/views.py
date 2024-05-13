from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(request):
   
    username = "keepmeposted.monash@gmail.com"  
    password = "aqsokzlapmzxvuev" 

    message = request.POST.get('message') # get message from data
    subject = request.POST.get('subject')  
    contacts = request.POST.get('contacts').split(',')
       

    for contact in contacts:
        email = MIMEMultipart("alternative")
        email["Subject"] = subject
        email["From"] = username
        email["To"] = contact


        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(message, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        email.attach(part1)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(username, password)
            server.sendmail(
                username, contact, email.as_string()
            )
            
    return JsonResponse({'details': "Emails sent successfully!"}, status=200)

