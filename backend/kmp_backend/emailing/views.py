from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import smtplib, ssl, markdown2
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


        # Convert message into plain MIMEText object
        part1 = MIMEText(message, "plain")

        # Convert message into HTML MIMEText object
        message_html = markdown2.markdown(message)
        part2 = MIMEText(message_html, "html")
    

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        email.attach(part1)
        email.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(username, password)
            server.sendmail(
                username, contact, email.as_string()
            )
            
    return JsonResponse({'details': "Emails sent successfully!"}, status=200)

