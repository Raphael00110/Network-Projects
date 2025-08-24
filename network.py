import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from useful import ConsoleTool
import time


while True:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # use 587
    server.starttls()
    server.ehlo()

    Mail = input("Enter Your Email: ")
    Password = input("Enter Your App Password: ")

    ConsoleTool.clear()
    server.login(Mail, Password)
    print("Login Successful!")
    time.sleep(2)
    ConsoleTool.clear()

    Receiver = input("Enter Receiver's Email: ")

    msg = MIMEMultipart()
    msg['From'] = Mail
    msg['To'] = Receiver

    ConsoleTool.clear()
    subject = input("Enter Subject: ")
    msg['Subject'] = subject

    message = input("Enter Message: ")
    msg.attach(MIMEText(message, 'plain'))
    ConsoleTool.clear()

    # Ask for attachment
    attach_choice = input("Would you like to attach a file? (y/n): ").strip().lower()
    if attach_choice == 'y':
        ConsoleTool.clear()
        file = input("Enter the file path: ").strip()
        with open(file, "rb") as attachment:
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f'attachment; filename={file}')
        msg.attach(p)

    # Send the email
    server.sendmail(Mail, Receiver, msg.as_string())
    ConsoleTool.line()
    print("Email Sent!")

    again = input("Press Y to send another email or any other key to exit: ").strip().lower()
    if again != 'y':
        server.quit()
        break
        ConsoleTool.clear()
