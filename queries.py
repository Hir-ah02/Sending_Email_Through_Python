import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender's email and password
your_email = "EmailAdress.com"
your_password = " Email App Password "

# Input recipient email address
to_email = "Email"

# Input email subject
subject = input("Enter the email subject: ")

# Input email bodyhey

body = input("Enter the email body: ")

# Create the email message
msg = MIMEMultipart()
msg["From"] = your_email
msg["To"] = to_email
msg["Subject"] = subject

# Attach the body of the email
msg.attach(MIMEText(body, "plain"))

# Connect to the SMTP server and send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(your_email, your_password)
    server.sendmail(your_email, to_email, msg.as_string())

print("Email sent successfully!")