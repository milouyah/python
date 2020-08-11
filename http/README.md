# HTTP

## [Requests: HTTP for Humans™](https://requests.readthedocs.io/en/master/)

### [Quick Start](https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request)

* Make a Request
  
```python
r = requests.get('https://api.github.com/events')
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')
```

* Passing Parameters In URLs¶
  
```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
``` 

* Response Content

```
r = requests.get('https://api.github.com/events')
r.text
```

* Binary Response Content
* JSON Response Content
```
r = requests.get('https://api.github.com/events')
r.json()
```
* Raw Response Content¶


* Custom Headers

```
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
```

* More complicated POST requests
* POST a Multipart-Encoded File
* Response Status Codes

```
r = requests.get('https://httpbin.org/get')
r.status_code
```

* Response Headers

```
r.headers
```

* Cookies¶

```
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

r.cookies['example_cookie_name']
'example_cookie_value'
```

* Redirection and History
* Timeouts
* Errors and Exceptions

Response.raise_for_status() will raise an HTTPError if the HTTP request returned an unsuccessful status code.