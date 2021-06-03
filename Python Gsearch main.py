import json
import requests
import smtplib
import Gsearchdata.txt
from requests.api import get, put
from email.parser import BytesParser
from email.policy import default
from email.message import EmailMessage
with open(Gsearchdata.txt) as fp

# requesting (var r) to get emails from source.  Emails consist of a structured sequence of sub-messages, each with their own set of headers and their own payload. 

r = requests.get("Gsearchdata.txt", params=None, payload=None, factory=EmailMessage, headers=None,r)
r.text
r.content
r.encoding
json = (r.json(JSONfile.py))
print(r.json)

#access db with loop
items = []
for item in json:
    items.append(item['JSONfile.py'])
print(items)

#define class email, which will search for the kwargs in the txt based on the policy
class email.parser.BytesFeedParser(_factory=None, *, policy=policy.compat32)
    feed(data)

class email.generator.BytesGenerator(outfp, mangle_from_=True, maxheaderlen=None, *, policy=None, linesep=None, raise_on_defect=False)
'''    
write(s)
Write s to the write method of the outfp passed to the Generator’s constructor. This provides just enough file-like API for Generator instances to be used in the print() function.
'''

class email.message.EmailMessage(policy=None, max_line_length=None,linesep=\r\n
    raise_on_defect=False
    max_line_length=None

class email.policy.EmailPolicy(**kw, utf8=True, refold_source=long)

def data(**kw):
    for key, value in kw.items():
        if key == data:
            return({**kw})


#place results from search file into db
'''
print(r.text)

output = open('JSONfile.py', 'w')
output.write(r.text)
output.close()
'''


#status code for testing reuest status:
'''
print(r.status_code)
 
if r:
print('Response OK')

else:
print('Response Failed')
'''
