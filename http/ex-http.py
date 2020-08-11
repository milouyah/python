
import requests

r = requests.get('https://api.github.com/user', auth=('id', 'passwd'))
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json())
