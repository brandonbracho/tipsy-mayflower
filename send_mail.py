import smtplib
from email.mime.text import MIMEText


def send_mail(name, email, password):
    port = 2525
    smtp_server = 'smtp.amiltrap.io'
    login = ''
    password = ''
    message = f""
