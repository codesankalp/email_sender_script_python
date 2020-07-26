import email.message
import mimetypes
import os.path
import smtplib
import getpass


def generate_email(sender, recipient, subject, body, attachment_path=None):
    '''Create email with attachment'''
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    #attachment
    if attachment_path: 
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/')

        with open(attachment_path, 'rb') as f:
            message.add_attachment(
                f.read(),
                maintype=mime_type,
                subtype = mime_subtype,
                filename=attachment_filename
            )
    return message


def send_message(message, smtp_server='smtp.gmail.com'):
    '''send mail to configured smtp server'''
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.set_debuglevel(0)
    email = input('email : ')
    password = getpass.getpass('Password ? : ')
    mail_server.login(email,password)
    mail_server.send_message(message)
    print("message sent.")
    mail_server.quit()
