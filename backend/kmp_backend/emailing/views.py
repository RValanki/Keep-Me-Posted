from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

api_key = "API-key"
list_id = 'list-ID'

data_center = api_key.split('-')[-1]

def send_email(request):
    message = request.POST.get('message') # get message from data 
    contacts = request.POST.get('contacts').split(',') # get contacts from data
    
    for i in contacts: # loop through contacts and add them as subscribers
        res = add_subscriber(i)
    
    return create_campaign_and_send(message) # create campaign and send the email
    



def add_subscriber(email):
    # Endpoint for adding a subscriber
    url = f'https://{data_center}.api.mailchimp.com/3.0/lists/{list_id}/members/'

    # Data for the new subscriber
    data = {
        "email_address": email,
        "status": "subscribed",  # or 'pending' if you want double opt-in
    }

    # Headers including Authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # POST request to add the subscriber
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Subscriber added successfully!")
        return True
    else:
        print("Failed to add subscriber:", response.text)
        return False
    
    
def create_campaign_and_send(message):
    subject = "KMP Meeting Summary"
    from_name = "KMP"
    reply_to = "kmp@gmail.com"

    create_url = f'https://{data_center}.api.mailchimp.com/3.0/campaigns'

    campaign_data = {
        "type": "regular",
        "recipients": {
            "list_id": list_id
        },
        "settings": {
            "subject_line": subject,
            "from_name": from_name,
            "reply_to": reply_to,
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Create campaign
    create_response = requests.post(create_url, json=campaign_data, headers=headers)
    if create_response.status_code != 200:
        return JsonResponse({'error': 'Failed to create campaign', 'details': create_response.text}, status=400)

    campaign_id = create_response.json().get('id')
    content_url = f'https://{data_center}.api.mailchimp.com/3.0/campaigns/{campaign_id}/content'
    content_data = {
        "html": f"<p>{message}</p>"
    }

    # Set content
    content_response = requests.put(content_url, json=content_data, headers=headers)
    if content_response.status_code != 200:
        return JsonResponse({'error': 'Failed to set campaign content', 'details': content_response.text}, status=400)

    send_url = f'https://{data_center}.api.mailchimp.com/3.0/campaigns/{campaign_id}/actions/send'

    # Send campaign
    send_response = requests.post(send_url, headers=headers)
    if send_response.status_code == 204:
        return JsonResponse({'details': "Campaign sent successfully!"}, status=200)
    else:
        return JsonResponse({'error': 'Failed to send campaign', 'details': send_response.text}, status=400)
