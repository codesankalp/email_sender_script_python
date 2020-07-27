from email_sender import generate_email, send_message
sender = input('Enter your mail : ')
reciever = input('Enter reciepent mail : ')
subject = input('Enter Subject: ')
body = input('Enter mail body : ')
attachment_path = input("Attachment path (leave blank if no attachment) : ")
if attachment_path == '': attachment_path = None
message = generate_email(sender,reciever,subject,body,attachment_path)
send_message(message)