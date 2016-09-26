#Author Ade Gbodimowo
#Script marks all emails from unread to read.

import imaplib
myemail = imaplib.IMAP4_SSL('imap.gmail.com', '993')
##Replace GMAILUSERNAMEHERE with your gmail username and PASSWORDHERE with your secret password
myemail.login('GMAILUSERNAMEHERE', 'PASSWORDHERE')
myemail.select('Inbox')
typ ,data = myemail.search(None,'UnSeen')
myemail.store(data[0].replace(' ',','),'+FLAGS','\Seen')
