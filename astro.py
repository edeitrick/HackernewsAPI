import requests

url = 'http://api.open-notify.org/astros.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
data1 = requests.get(url, headers=headers)
data2 = data1.json()
print(f"Status Code: {data1.status_code}")
for info in data2['people'][:5]:
  print(info['name'])



