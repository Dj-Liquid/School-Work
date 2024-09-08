from send_email import EmailSender


# Example usage:
sender_email = "sici3902@gmail.com"
receiver_email = "robinsond993@gmail.com"#sici3902@gmail.com
password = "euck qnjq kobv isro"  # If you're using Gmail, you might need to generate an app password Test12345678!@#

email_sender = EmailSender(sender_email, receiver_email, password)
subject = "Test Email from Python"
body = "XXXXXX ALERT XXXXXX\
        \n\nAttention! SCOTIABANK JUNCTION BRANCH is currently in an altercation with dangerous suspects.\
        \n\nSuspect is:\
        \nArmed and Dangerous\
        \n\n\nSuspect vehicle is:\
        \nUnidentified"

email_sender.send_email(subject, body)