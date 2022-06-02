import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# connect with Google's servers
SMTP_SSL_HOST = 'smtp.gmail.com'
SMTP_SSL_PORT = 465

# use username or email to log in
DEFAULT_USERNAME = 'senderSMTP001@gmail.com'
DEFAULT_PASSWORD = 'sender1234'

# TODO
# Functions -> create format html files to response for each functions => sender.py
# - List -> Stop or Kill processes and apps
# - Shutdown & reset?
# - Capture screenshot & webcam
# - Record webcam in X seconds
# - Update registry value
# - Key logger
# - Copy file


class Sender():
    def __init__(self, username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD):
        self.server = smtplib.SMTP_SSL(SMTP_SSL_HOST, SMTP_SSL_PORT)
        self.server.login(username, password)
        self.addrs = username

    def send_mail(self, to_addrs, subject, content):
        message = MIMEText(content)
        message['subject'] = subject
        message['from'] = self.addrs
        message['to'] = ', '.join(to_addrs)
        self.server.sendmail(self.addrs, to_addrs, message.as_string())

    # def reply(self):

    def quit(self):
        self.server.quit()


S = Sender()
S.send_mail(['receiverimap002@gmail.com'], 'RDM-LIST PROCESS', '')
S.send_mail(['receiverimap002@gmail.com'], 'RDM-LIST APP', '')
S.send_mail(['receiverimap002@gmail.com'], 'RDM-KEYLOGGER', '20')
S.quit()
