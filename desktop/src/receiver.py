import email
import imaplib

IMAP_SSL_HOST = 'imap.gmail.com'

# use username or email to log in
DEFAULT_USERNAME = 'receiverimap002@gmail.com'
DEFAULT_PASSWORD = 'receiver1234'


class Receiver():
    def __init__(self, username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD):
        # connect to the server and go to its inbox
        self.mail = imaplib.IMAP4_SSL(IMAP_SSL_HOST)
        self.mail.login(username, password)
        # we choose the inbox but you can select others
        self.mail.select('inbox')

    def get_recent_mail(self):
        status, data = self.mail.search(None, 'ALL')

        mail_ids = data[-1].split()

        i = mail_ids[-1]
        status, data = self.mail.fetch(i, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                mail_from = message['from']
                mail_subject = message['subject']
                if message.is_multipart():
                    mail_content = ''
                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()
                print(f'From: {mail_from}')
                print(f'Subject: {mail_subject}')
                print(f'Content: {mail_content}')


R = Receiver()
R.get_recent_mail()