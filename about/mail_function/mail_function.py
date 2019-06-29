import smtplib
from email.message import EmailMessage
from .mail_function_config import email_address, email_password, email_receiver_list, email_subject


def mail_to_me(name, email, comments):
    msg = EmailMessage()
    msg["From"] = email_address
    msg["To"] = email_receiver_list
    msg["Subject"] = email_subject
    host = "smtp.gmail.com"
    port = 465

    # generate content
    html_content = f'<html><body><table><tr><td>Name</td><td>{name}</td></tr><tr><td>Email</td><td>{email}</td></tr><tr><td>Comments</td><td>{comments}</td></tr></table></body></html>'

    # attach content to email
    msg.add_alternative(html_content, subtype="html")

    # login with SSL & send email
    with smtplib.SMTP_SSL(host, port) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
