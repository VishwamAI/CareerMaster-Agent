import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPException, SMTPAuthenticationError, SMTPConnectError, SMTPHeloError, SMTPSenderRefused, SMTPRecipientsRefused, SMTPDataError

# Configure logging
logging.basicConfig(level=logging.INFO)

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

        logging.info(f"Email sent successfully to {to_email}")

    except SMTPAuthenticationError:
        logging.info(f"Failed to send email to {to_email}. Error: Authentication failed.")
    except SMTPConnectError:
        logging.info(f"Failed to send email to {to_email}. Error: Unable to connect to the SMTP server.")
    except SMTPHeloError:
        logging.info(f"Failed to send email to {to_email}. Error: The server refused the HELO message.")
    except SMTPSenderRefused:
        logging.info(f"Failed to send email to {to_email}. Error: The server refused the sender address.")
    except SMTPRecipientsRefused:
        logging.info(f"Failed to send email to {to_email}. Error: The server refused the recipient address.")
    except SMTPDataError:
        logging.info(f"Failed to send email to {to_email}. Error: The server replied with an unexpected error code.")
    except SMTPException as e:
        logging.info(f"Failed to send email to {to_email}. SMTP error occurred: {str(e)}")
    except Exception as e:
        logging.info(f"Failed to send email to {to_email}. Error: {str(e)}")

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
