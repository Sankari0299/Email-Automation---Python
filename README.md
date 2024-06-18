# Email Automation Project

## Overview

The Email Automation Project aims to streamline the process of sending emails using Python. This project provides a simple script to send an email using the SMTP protocol. It covers setting up email content, connecting to the email server, and sending the email.

## Features

- **Email Sending**: Send emails using Python.
- **Customizable Email Content**: Define your email's sender, recipient, subject, and body.

## Dependencies

This project relies on the `smtplib` and `email` libraries, which are included in Python's standard library.

## Installation and Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/email-automation.git
   cd email-automation
   ```

2. **Setup Email Credentials**:
   - Open the `email_automation.py` script.
   - Replace the placeholder values with your email credentials and details:
     ```python
     email_user = "your-email@example.com"  # Your email ID
     email_sender = "receiver-email@example.com"  # Receiver's email ID
     subject = "Your Email Subject"  # Your email subject
     body = "Your email body message"  # Your email body message
     password = "your-email-password"  # Your email password
     ```

## Usage

To send an email using the provided script, follow these steps:

1. **Update the Script**:
   - Modify the `email_automation.py` script with your email details.

2. **Run the Script**:
   - Execute the script using Python:
     ```sh
     python email_automation.py
     ```

## Code Explanation

Here is a breakdown of the provided script:

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Defining data
email_user = "your-email@example.com"  # Your email ID
email_sender = "receiver-email@example.com"  # Receiver's email ID
subject = "Your Email Subject"  # Your email subject
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_sender
msg['Subject'] = subject
body = "Your email body message"  # Your email body message
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

# Connecting to the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, "your-email-password")  # Your email password

# Sending the email
server.sendmail(email_user, email_sender, text)
server.quit()
```

### Script Details

1. **Importing Libraries**:
   - `smtplib`: For sending emails using the SMTP protocol.
   - `email.mime.multipart.MIMEMultipart` and `email.mime.text.MIMEText`: For constructing the email message.

2. **Defining Email Data**:
   - `email_user`: The sender's email address.
   - `email_sender`: The receiver's email address.
   - `subject`: The subject of the email.
   - `body`: The body content of the email.

3. **Setting Up the Email Message**:
   - Construct a multipart email message with the subject, sender, and receiver.
   - Attach the body text to the email message.

4. **Connecting to the SMTP Server**:
   - Connect to Gmail's SMTP server (`smtp.gmail.com`) on port 587.
   - Start TLS encryption for security.
   - Log in to the email server using the sender's credentials.

5. **Sending the Email**:
   - Send the constructed email message from the sender to the receiver.
   - Quit the server connection after sending the email.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.


