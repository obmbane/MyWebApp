import smtplib, ssl, os

def send_email(message):

    host = 'smtp.gmail.com'
    port = 465

    username = os.getenv("MY_EMAIL")
    password = os.getenv("MYAPP_PASSWORD")
    receiver = os.getenv("MY_EMAIL")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:

        server.login(username,password)
        server.sendmail(username, receiver,message)


