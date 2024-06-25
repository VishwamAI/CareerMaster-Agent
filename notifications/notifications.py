import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_notification(to_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
    try:
        # Set up the MIME
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the message to the MIME
        msg.attach(MIMEText(message, 'plain'))

        # Create SMTP session for sending the mail
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable security
        server.login(smtp_username, smtp_password)  # Login with SMTP server credentials
        text = msg.as_string()
        server.sendmail(smtp_username, to_email, text)
        server.quit()

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")

if __name__ == "__main__":
    # Example usage
    to_email = "user@example.com"
    subject = "Job Application Submitted"
    message = "Your job application has been successfully submitted."
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your_smtp_username"
    smtp_password = "your_smtp_password"

    send_email_notification(to_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password)
