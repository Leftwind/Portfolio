import smtplib, ssl



#Needs things
def send_email(message):
    host = 'smtp.gmail.com'
    port = 465


    username = 'andreslozano0123@gmail.com'
    password = 'scnc eyvz yobs dase'

    receiver = 'andreslozano0123@gmail.com'

    context = ssl.create_default_context()

        
    with smtplib.SMTP_SSL(host, port, context=context) as server: 
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__=='__main__':
    send_email()