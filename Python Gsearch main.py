import pandas as pd
import json
import requests
import smtplib
#import Gsearchdata.txt
from requests.api import get, put
from email.parser import BytesParser
from email.policy import default
from email.message import EmailMessage
from imaplib import IMAP4
with IMAP4("https://github.com/mspaldingworks/Python-May-2021/blob/ea9f7788a05a3d0703cfe9ecf0835dd70dc07234/Gsearchdata.txt") as M:
    M.noop()
#with open(Gsearchdata.txt) as fp

# requesting (var req) to get emails from source.  Emails consist of a structured sequence of sub-messages, each with their own set of headers and their own payload. 

req = requests.get("https://github.com/mspaldingworks/Python-May-2021/blob/ea9f7788a05a3d0703cfe9ecf0835dd70dc07234/Gsearchdata.txt")
req.text
req.content
req.encoding
json = (r.json(JSONfile.py))
print(r.json)

class imaplib.IMAP4(host='')

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

def emails_between(suspects):
    # List the email objects
    emails = []
    # Walking through the directory
    for root, dirs, files in os.walk('enron_email_corpus'):
        for i in files:
            file_path = os.path.join(root, i)
            with open('%s' % file_path, 'r') as fp:
                headers = Parser().parse(fp)
                if headers['To'] == suspects.values() and headers['From'] == suspects.values():
                    emails.append(fp.message.Message)
    return emails
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
