from os import system
system("git pull")
system("clear")
"""

You should unable 2-Step Verification, Then get your password from google apppasswords.

"""
print("hello, world!")
try:
    import smtplib
    import ssl
    from email.message import EmailMessage
    from getpass import getpass
    
    # Define email sender and receiver
    email_sender = input("Enter Your Email: ")
    email_password = getpass('Enter Your Password: ')
    email_receiver = input('Enter The Receiver Email: ')
    
    # Set the subject and body of the email
    subject = input('Enter The Subject: ')
    body = input("Enter The Body: ")
    
    # Set the times of send
    Message = EmailMessage()
    Message['From'] = email_sender
    Message['To'] = email_receiver
    Message['Subject'] = subject
    Message.set_content(body)
    
    # Add SSL (layer of security)
    context = ssl.create_default_context()
    
    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as App: 
        App.login(email_sender, email_password)
        App.sendmail(email_sender, email_receiver, Message.as_string())
    print("Email has been sent.")
except:
    print("An error")
