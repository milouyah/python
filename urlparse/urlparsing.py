from urllib.parse import urlparse

o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
print(o)
print(o.scheme)
print(o.port)
print(o.geturl())