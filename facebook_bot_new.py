import requests
import json

url = "https://graph.facebook.com/102888708318630/feed"

payload = json.dumps({
  "access_token": "EAACpTRXZBREcBAKxHz2WotpSx9X6uIkEkH6Din3a0Eea6MLDtCIDFa8kIZBAVabUmfkRRXZCOROa9DudU6GB6HB9KpEOP9IqMkP6hLwhG5yeeVl15x9pmlH1bh5ZBKYQidAmbu1eDvUtsZBkcb3GrgegxZA4CeYJBe3nOqPb8S0Uj4yuhcKFH3",
  "message": "Hello, Facebook Page!"
})
headers = {
  'Content-Type': 'application/json',
  'User-Agent':'PostmanRuntime/7.26.10'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
