from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
# Create your views here.

api_key = "API-key"
list_id = 'list-ID'

data_center = api_key.split('-')[-1]

def add_subscriber(request):
    """
    Sends an email using the Mailchimp API with a hardcoded API key.
    :param request: JSON data that will hold contacts and email content
    """
    print("Send email function triggered")

    email = 'example@gmail.com'
    first_name = 'John'
    last_name = 'Smith'
    # Endpoint for adding a subscriber
    url = f'https://{data_center}.api.mailchimp.com/3.0/lists/{list_id}/members/'

    # Data for the new subscriber
    data = {
        "email_address": email,
        "status": "subscribed",  # or 'pending' if you want double opt-in
        "merge_fields": {
            "FNAME": first_name,
            "LNAME": last_name
        }
    }

    # Headers including Authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # POST request to add the subscriber
    response = requests.post(url, json=data, headers=headers)

    # if response.status_code == 200:
    #     print("Subscriber added successfully!")
    # else:
    #     print("Failed to add subscriber:", response.text)

    # return HttpResponse(response.status_code)
    return add_and_send_campaign(request)





def add_and_send_campaign(request):
    """
    Creates and sends an email campaign using the Mailchimp API.
    This function takes a request object containing the necessary configuration and credentials,
    creates a new email campaign, sets the campaign content, and attempts to send the campaign.
    Parameters:
    - request (HttpRequest): The HTTP request object that may contain additional parameters such as data center identifier,
      API key, list ID, etc. These parameters are expected to be accessible as attributes or through a specific method like GET/POST.
    Returns:
    - HttpResponse: Returns an HttpResponse indicating the success of the operation, including sending the campaign or any errors encountered.
      If the campaign creation, content setting, or sending fails, it returns a JsonResponse detailing the error and the respective HTTP status code.
    
    # send with mailchimp here
    Raises:
    - HttpResponse with status 500 if it encounters an unhandled case.
    """
    subject = "test campaign"
    from_name = "Joe"
    reply_to = "example@gmail.com"

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
            "to_name": "*|FNAME|* *|LNAME|*"
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
        "html": "<p>Hello, this is a test email</p>"
    }

    # Set content
    content_response = requests.put(content_url, json=content_data, headers=headers)
    if content_response.status_code != 200:
        return JsonResponse({'error': 'Failed to set campaign content', 'details': content_response.text}, status=400)

    send_url = f'https://{data_center}.api.mailchimp.com/3.0/campaigns/{campaign_id}/actions/send'

  # Send campaign
    send_response = requests.post(send_url, headers=headers)
    if send_response.status_code == 204:
        return HttpResponse("Campaign sent successfully!")
    else:
        return JsonResponse({'error': 'Failed to send campaign', 'details': send_response.text}, status=400)
