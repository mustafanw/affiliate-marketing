import http.client
import json

conn = http.client.HTTPSConnection("graph.facebook.com")
payload = json.dumps({
  "access_token": "EAACpTRXZBREcBAML9dMuPcK0TNWggPZAcII93MnFvrQt8h47HePwu0xl2SbkZBxqbSc5wSELAKT9D7I4MO9RKW8kJTfLp21yL6dDXwPCZAd17JycnTcTX8dO0vdwrexZBv4xYN7ZBhqxDFysWqMWrfvxFs7aflQTtZC52hucQBSffJjrWOTpqayz8J0rs4IakuTVYJxJymMwLXTkZBfE6eZCL",
  "message": "Hello, Facebook Page!"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/102888708318630/feed", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))