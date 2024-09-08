import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class EmailSender:
    def __init__(self, sender_email, receiver_email, password):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.password = password

    def send_email(self, subject, body,_):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = self.receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))
        if(_ is not None):
            message.attach(_)
            

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(self.sender_email, self.password)
            text = message.as_string()
            server.sendmail(self.sender_email, self.receiver_email, text)

        print("Email sent successfully!")


