import http.client
import json

conn = http.client.HTTPSConnection("graph.facebook.com")
payload = json.dumps({
  "access_token": "EAACpTRXZBREcBAFO2OblkTUzXGcrBan3uUGjMljfxeVVqtoppdXvofVrERbzFjhHET51zq3T4HzNj9yEWH3WB4FNTNsUloL6y8wbNPGyyFZCd5hDyP7j2It0mlDvZAu53ZC9llBtEz2bFWMNY0Y20I1RZAVBJoSgywTu9Wdx2fe22rtZAfphpf",
  "message": "Hello, Facebook Page!"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/102888708318630/feed", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))