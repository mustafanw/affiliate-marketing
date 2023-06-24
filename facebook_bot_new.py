import requests

# Define the page access token and page ID
access_token = 'EAACpTRXZBREcBAKCicYvnmZBCfZCRoZBA7YscRzucNL1vWgO4iYOWOBJCEpxjKdxO0876xSzMeclhU9BkEspZAKD8E693ZBVyqSS8TIA5ptk1qkWA8otXLh3JoayNla21GAo3fsrMBJ4LXZCmVxbu1ZCDtfSjqx8457L46zkXSjK6tsMlEP6ruqe'
page_id = '102888708318630'

# Define the API endpoint
api_endpoint = f'https://graph.facebook.com/{page_id}/feed'

# Define the post parameters
post_params = {
    'access_token': access_token,
    'message': 'Hello, Facebook Page!'
}

# Make the API POST request
response = requests.post(api_endpoint, data=post_params)

# Check the response status
if response.status_code == 200:
    print('Post created successfully!')
else:
    print('Error creating post:', response.text)
