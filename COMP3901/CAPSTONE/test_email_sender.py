import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class EmailSender:
    def __init__(self, sender_email, receiver_emails, password):
        self.sender_email = sender_email
        self.receiver_emails = receiver_emails
        self.password = password

    def send_email(self, subject, body, attachment=None):
        # Check if receiver_emails is a string
        if isinstance(self.receiver_emails, str):
            # If it's a string, convert it to a list with a single element
            receiver_emails = [self.receiver_emails]
        else:
            # If it's already a list, use it as is
            receiver_emails = self.receiver_emails

        for receiver_email in receiver_emails:
            try:
                message = MIMEMultipart()
                message["From"] = self.sender_email
                message["To"] = receiver_email
                message["Subject"] = subject

                message.attach(MIMEText(body, "plain"))
                if attachment is not None:
                    message.attach(attachment)

                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(self.sender_email, self.password)
                    text = message.as_string()
                    server.sendmail(self.sender_email, receiver_email, text)

                print("Email sent successfully to", receiver_email)
            except smtplib.SMTPRecipientsRefused as e:
                print("Failed to send email to", receiver_email, ":", e)
            except Exception as e:
                print("An error occurred while sending email to", receiver_email, ":", e)
