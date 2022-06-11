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
from utils.configs import *
import os

# Configurations of services
SMTP_SSL_PORT = 465
SMTP_SSL_HOST = 'smtp.gmail.com'
IMAP_SSL_HOST = 'imap.gmail.com'

# Subject of mail
RECOGNIZE_SUBJECT = 'RDM'
COMMANDS = ['HELP', 'LIST PROCESS', 'KILL PROCESS',
            'LIST APP', 'KILL APP',
            'CAPTURE SCREEN', 'RECORD SCREEN',
            'SHOT WEBCAM', 'RECORD WEBCAM',
            'VIEW FILE SYSTEM', 'COPY FILE SYSTEM', 'DOWNLOAD FILE SYSTEM',
            'KEYLOGGER',
            'SHUTDOWN', 'RESTART',
            'WRITE REGISTRY', 'GET REGISTRY', 'CREATE REGISTRY', 'SET REGISTRY', 'DELETE VALUE REGISTRY', 'DELETE KEY REGISTRY']


# Templates
TEMPLATE_PATH = 'templates'
TEMPLATE_FILE_NAMES = {'LIST PROCESS': 'list-process.html',
                       'KILL PROCESS': 'kill-process.html',
                       'LIST APP': 'list-app.html',
                       'KILL APP': 'kill-app.html',
                       'CAPTURE SCREEN': 'capture-screen.html',
                       'RECORD SCREEN': 'record-screen.html',
                       'SHOT WEBCAM': 'shot-webcam.html',
                       'RECORD WEBCAM': 'record-webcam.html',
                       'VIEW FILE SYSTEM': 'file-system.html',
                       'COPY FILE SYSTEM': 'copy-file-system.html',
                       'DOWNLOAD FILE SYSTEM': 'download-file-system.html',
                       'KEYLOGGER': 'keylogger.html',
                       'SHUTDOWN': 'shutdown.html',
                       'RESTART': 'restart.html',
                       'WRITE REGISTRY': 'write-registry.html',
                       'GET REGISTRY': 'get-registry.html',
                       'CREATE REGISTRY': 'create-registry.html',
                       'SET REGISTRY': 'set-registry.html',
                       'DELETE VALUE REGISTRY': 'delete-value-registry.html',
                       'DELETE KEY REGISTRY': 'delete-key-registry.html',
                       'HELP': 'guide.html', }


class Receiver():
    """A Receiver for reading and auto-replying 
    """

    def __init__(self):
        """Inits Receiver with username, password, trusted senter, and configurations for server

        """
        self.username, self.password, self.trusted_sender = get_configs()
        self.server = smtplib.SMTP_SSL(SMTP_SSL_HOST, SMTP_SSL_PORT)
        self.server.login(self.username, self.password)
        self.addrs = self.username
        # connect to the server and go to its inbox
        self.mail = imaplib.IMAP4_SSL(IMAP_SSL_HOST)
        self.mail.login(self.username, self.password)
        # we choose the inbox but you can select others
        self.mail.select('inbox')

    def get_unanswered_mails(self):
        """Get unanswered mails

        :return: (list) a list of unanswered mails
        """
        self.mail.select(readonly=False)
        _, data = self.mail.search(None, '(UNANSWERED)')
        self.mail.close()
        return data[0].split()

    def is_valid_mail(self, mail_number):
        """Check if a mail satisfied with conditions

        :param mail_number: (str)
        :return: (str, str) as command, parameter of command
        """
        self.mail.select(readonly=True)
        _, data = self.mail.fetch(mail_number, '(RFC822)')
        self.mail.close()
        mail = email.message_from_bytes(data[0][1])

        mail_from = mail['From'].split()[-1][1:-1]
        mail_subject = mail['Subject']
        if mail.is_multipart():
            mail_content = ''
            for part in mail.get_payload():
                if part.get_content_type() == 'text/plain':
                    mail_content += part.get_payload()
        else:
            mail_content = mail.get_payload()
        mail_content = mail_content.replace('\r\n', '')

        print(f'From: {mail_from}')
        print(f'Subject: {mail_subject}')
        print(f'Content: {mail_content}')

        if mail_from not in self.trusted_sender:
            return None, None

        subject, command_subject = mail_subject.split('-')

        if subject != RECOGNIZE_SUBJECT or command_subject not in COMMANDS:
            return None, None

        print('-> This mail is valid')

        return command_subject, mail_content

    def reply(self, mail_number, content):
        """Reply mail with mail number and mark 

        :param mail_number: (str)
        :param content: (str)
        """
        self.mail.select(readonly=True)
        _, data = self.mail.fetch(mail_number, '(RFC822)')
        self.mail.close()
        self.send_auto_reply(email.message_from_bytes(data[0][1]), content)
        self.mail.select(readonly=False)
        self.mail.store(mail_number, '+FLAGS', '\\Answered')
        self.mail.close()

    def create_auto_reply(self, original, content):
        """Create the reply mail of original mail

        :param original: (mail)
        :param content: (str)
        :return: (mail) a replied mail with content
        """
        mail = MIMEMultipart('alternative')
        mail['Message-ID'] = make_msgid()
        mail['References'] = mail['In-Reply-To'] = original['Message-ID']
        mail['Subject'] = 'Re: ' + original['Subject']
        mail['From'] = self.addrs
        mail['To'] = original['Reply-To'] or original['From']

        # get template command email from command
        command = original['Subject'].split('-')[1]
        if content == False:
            template = os.path.join(
                TEMPLATE_PATH, 'wrong_execute.html')
            body_html = open(template)
            body_html = body_html.read()
            body_html = body_html.format(content)
        elif content == 'WrongSyntaxError404':
            template = os.path.join(
                TEMPLATE_PATH, 'wrong_syntax.html')
            body_html = open(template)
            body_html = body_html.read()
            body_html = body_html.format(content)
        elif content == 'AskForHelp':
            template = os.path.join(
                TEMPLATE_PATH, 'guide.html')
            body_html = open(template)
            body_html = body_html.read()
            body_html = body_html.format(content)
        else:
            template = os.path.join(
                TEMPLATE_PATH, TEMPLATE_FILE_NAMES[command])
            body_html = open(template)
            body_html = body_html.read()

            if command == 'LIST PROCESS' or command == 'LIST APP':
                content_str = str(content)
                data_str = content_str.replace("\n", " ")
                data = data_str.split(" ")
                size = len(data)
                i = 0
                while i < size:
                    if data[i] == '':
                        del data[i]
                        i = i - 1
                        size = len(data)
                        continue
                    i += 1

                if command == 'LIST PROCESS':
                    for i in range(len(data) - 1):
                        if data[i] == "Memory" and data[i + 1] == "Compression":
                            data[i] += " " + data[i + 1]
                            del data[i + 1]
                            break

                #  loop over our arrays and create our html string
                outputHTML = "<table>"
                for i in range(len(data)//3):
                    if i == 1:
                        continue
                    if i == 0:
                        outputHTML += "<tr class = \"header_table\">"
                    else:
                        outputHTML += "<tr>"
                    for j in range(3):
                        if j == 1:
                            outputHTML += "<td style=\"width:30%\">"
                        else:
                            outputHTML += "<td>"
                        outputHTML += data[3 * i + j] + "</td>"
                    outputHTML += "</tr>"
                outputHTML += "</table>"
                body_html = body_html.format(outputHTML)
            elif command == 'VIEW FILE SYSTEM':
                content_list = list(content)
                root = content_list[-1]
                outputHTML = "<ul><li class=\"root_dir\">{}<ul>".format(root)
                for i in range(len(content_list) - 1):
                    if os.path.isfile(os.path.join(root, content_list[i])):
                        outputHTML += "<li class=\"child_dir_2\">" + \
                            content_list[i] + "</li>"
                    else:
                        outputHTML += "<li class=\"child_dir_1\">" + \
                            content_list[i] + "</li>"

                outputHTML += "</ul></li></ul>"
                body_html = body_html.format(outputHTML)
            else:
                body_html = body_html.format(content)

        # attach html
        mail.attach(MIMEText(body_html, 'html'))

        # attach files
        file_name = None
        if command in ['CAPTURE SCREEN', 'RECORD SCREEN', 'SHOT WEBCAM', 'RECORD WEBCAM', 'DOWNLOAD FILE SYSTEM']:
            file_name = content
            if command != 'DOWNLOAD FILE SYSTEM':
                file_name = os.path.join('.temp', file_name)

            mail.attach(self.attach_file(file_name))

        return mail

    def send_auto_reply(self, original, content):
        """Send the reply mail

        :param original: (mail)
        :param content: (str)
        """
        self.server.sendmail(
            self.addrs, [original['From']],
            self.create_auto_reply(original, content).as_bytes())
        log = 'Replied to “%s” for the mail “%s”' % (original['From'],
                                                     original['Subject'])
        print(log)

    def attach_file(self, file_name):
        """Attach files 

        :param file_name: (str)
        :return: (mail) a mail with attached file
        """
        try:
            with open(file_name, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header("Content-Disposition",
                            f"attachment; filename= {os.path.basename(file_name)}",)

            return part

        except Exception as e:
            print(f'Oh no! We didn\'t found the attachment!\n{e}')
            return None

    def quit(self):
        """Quit server

        """
        self.server.quit()
