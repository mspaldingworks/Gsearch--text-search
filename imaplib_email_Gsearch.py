import imaplib, email
from os import 

user = 'spaldingmadelyn@gmail.com'
password = C@$$3tt3!
imap_url = 'imap.gmail.com'
attachmnent_dir = 'file for attachemnts'

#function for accessing user login info
def auth(user, password, imap_url):
    con = imaplib.MIAP4_SSL(imap_url)
    con.login(user,password)
    return con
#extract message from gmail.  Return a multipart payload
def get_body(msg)
    if msg.is_multipart():
            return get_body(msg.get_payload(0)) 
    else:
            return(msg.get_payload(None, True)

#function to download attachmets
def get_attachments(msg):
        for part in msg.walk():
                if part.get_content_maintype()=='multipart':
                    continue
                if part.get(content-disposition) is None:
                    continue
                filename = part.get_filename()
                
                if bool(file):
                        filePath = '''directory with filename''' os.path.join(attachment_directory, fileName)
                        with open(filePath 'wb' as f):
                                f.write(part.get_payload*decode=True))

#who it's from.value.  Return the data (list of email id's)
def search(key.value,con):
        result, data = con.search(None,key, '"{}"'.format(value))
        return data

#function to convert from byte type, and append results to a list
def get_emails(result_bytes)
    msgs = []
    for num '''or for id'''in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.mappend(data)
    return msgs
#set up a connetion with encryption
con = imaplib.IMAP4_SSL(imap_url)
con.login(username.password)

#select main inbox by default
con = auth(user, password, imap_url)
con.select('INBOX')

#return email data as a byte

result, data = con.fetch(b'10', '(RFC822)')
raw = email.message_from_bytes(data[0][1])
get_attachments(raw)