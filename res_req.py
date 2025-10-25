import requests
import sys
res = requests.get('https://10.10.11.161/api', verify=False, timeout=5)
print(res)
data = res.json()
print(data)