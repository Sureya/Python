import pycurl
import StringIO
import json

c = pycurl.Curl()
url  = raw_input("URL : ")
c.setopt(pycurl.URL, url)

b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.MAXREDIRS, 5)
c.perform()
html = b.getvalue()

inputs  = json.loads(html)

key_lis =  inputs.keys()


print len(inputs.keys())

