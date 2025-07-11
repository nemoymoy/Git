import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MyMail:
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(
            self,
            login='login@gmail.com',
            password='qwerty',
            subject='Subject',
            recipients=('vasya@email.com', 'petya@email.com'),
            message='Message',
            header=None
    ):
        self.login = login
        self.password = password
        self.subject = subject
        self.list_recipients = recipients #['vasya@email.com', 'petya@email.com']
        self.message = message
        self.header = header

    def send_message(self):
        mime_object = MIMEMultipart()
        mime_object['From'] = self.login
        mime_object['To'] = ', '.join(self.list_recipients)
        mime_object['Subject'] = self.subject
        mime_object.attach(MIMEText(self.message))
        return mime_object

    def create_smtp_session(self, port=587):
        smtp_object = smtplib.SMTP(self.GMAIL_SMTP, port)
        smtp_object.ehlo()
        smtp_object.starttls()
        smtp_object.ehlo()

        smtp_object.login(self.login, self.password)
        for recipient in self.list_recipients:
            smtp_object.sendmail(self.login, recipient, self.send_message().as_string())
        smtp_object.quit()

    def connecting_imap_server(self):
        imap_server = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        imap_server.login(self.login, self.password)
        return imap_server

    def fetch_message(self, mail_box='inbox'):
        imap_server = self.connecting_imap_server()
        mail_boxes = imap_server.list()
        if mail_box in mail_boxes:
            imap_server.select(mail_box)
            criterion_string = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
            _result_search, data_search = imap_server.search(None, criterion_string)
            assert data_search[0], 'There are no letters with current header'
            email_messages = dict()
            for num in data_search[0].split():
                _type_fetch, data_fetch = imap_server.fetch(num, '(RFC822)')[0]
                email_messages[num] = email.message_from_string(data_fetch[0][1])
                imap_server.close()
                imap_server.logout()
            return email_messages
        else:
            print(f'Mail box {mail_box} not exist')
            imap_server.close()
            imap_server.logout()
            return None

if __name__ == "__main__":
    instance_of_the_class_mail = MyMail()