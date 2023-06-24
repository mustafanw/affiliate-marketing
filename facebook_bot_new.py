import requests

# Define the page access token and page ID
access_token = 'EAACpTRXZBREcBAGVSJFQ5ZCArumW3DcklnfqgT9DXjeZAZAsrWHv8ZCJPZC9O8UgWet1Ll4gMlmTmtVPS15M0W8WS0ZCYTNZC2Sqs4lPGZAHLCmFEr5Llp4PdZBUhaZAKpAau8FcYlDZBMLT1eCLSYNRYrSWTTi0f3mpAz0Y1qtmPwc60ejbslIYFskq'
page_id = '102888708318630'
HEADERS={

"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",

}
# Define the API endpoint
api_endpoint = f'https://graph.facebook.com/{page_id}/feed'

# Define the post parameters
post_params = {
    'access_token': access_token,
    'message': 'Hello, Facebook Page!'
}

# Make the API POST request
response = requests.post(api_endpoint, data=post_params, headers=HEADERS)

# Check the response status
if response.status_code == 200:
    print('Post created successfully!')
else:
    print('Error creating post:', response.text)
