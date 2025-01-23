# Email Event Reminder Script
This repository contains a Python script that sends email invitations for a scheduled meeting. The script allows you to customize the event details such as the date, time, and recipients of the invitation.

## 0 - Overview
The script reads data from a .env file for sensitive information (e.g., email credentials) and a recipients.json file for the list of email recipients. It uses an HTML template for the email body, which can be easily customized. You can execute the script via the command line interface (CLI) and specify the event date and time.

## 1 - Requirements
- Python 3.7+
- pip (Python package installer)
- Access to an SMTP server (e.g., SMTP for Aruba, Gmail, etc.)
## 1.1 - Installation
### 1.1.1 - Clone the repository
To get started, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/email-event-reminder.git
cd email-event-reminder
```

### 2.2 -Setup Virtual Environment
Create and activate a virtual environment to manage dependencies:

```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### 2.3 - Install Dependencies
Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```
## 3 - Configuration
### 3.1 - .env File
Create a .env file in the root of the project directory to store sensitive information such as your email credentials. The .env file should contain the following variables:

```env
EMAIL=your-email@example.com
PASSWORD=your-email-password
SMTP_SERVER=smtp.your-email-provider.com
SMTP_PORT=465  # Or 587 for some providers
Replace the values with your actual email account and SMTP server details.
```

### 3.2 - recipients.json File
This file contains the list of recipients to whom the invitation emails will be sent. Create a recipients.json file with the following structure:

```json
Copia
Modifica
{
  "destinatari": [
    "giacomo.fiorucci@emotion-team.com",
    "kevin.bodan@emotion-team.com",
    "c.calcagni@emotion-team.com",
    "christopher.caponi@emotion-team.com",
    "filippo.mariani@emotion-team.com",
    "giulio.cassano@emotion-team.com",
    "francesco.bellesini@emotion-team.com",
    "e.mancinelli@emotion-team.com",
    "massimo.briceno@emotion-team.com"
  ]
}
```
Add or remove email addresses in the "destinatari" list as needed. The script will read this file and send the email invitations to all the recipients listed.

### 3.3 - Email Template (mailto_event_reminder.html)
The email body is rendered from an HTML template located in the mailto_event_reminder.html file. You can modify the content and design of this template as needed. The placeholders in the template, such as {data_riunione}, {ora_riunione}, {mailto_conferma}, and {mailto_rifiuto}, will be replaced with the actual event data when sending the email.

Here’s an example of the HTML template:

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .button {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            border-radius: 5px;
            margin: 5px;
        }
        .button.red {
            background-color: #f44336;
        }
    </style>
</head>
<body>
    <p>Dear Colleague,</p>
    <p>You are invited to attend the following company meeting:</p>
    <ul>
        <li><strong>Date:</strong> {data_riunione}</li>
        <li><strong>Time:</strong> {ora_riunione}</li>
        <li><strong>Location:</strong> Meeting Room</li>
    </ul>
    <p>Please confirm your attendance by clicking one of the buttons below:</p>
    <a href="{mailto_conferma}" class="button">Confirm Attendance</a>
    <a href="{mailto_rifiuto}" class="button red">Cannot Attend</a>
    <p>Thank you!</p>
</body>
</html>
```
<!DOCTYPE html>
<html>
<head>
    <style>
        .button {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            border-radius: 5px;
            margin: 5px;
        }
        .button.red {
            background-color: #f44336;
        }
    </style>
</head>
<body>
    <p>Dear Colleague,</p>
    <p>You are invited to attend the following company meeting:</p>
    <ul>
        <li><strong>Date:</strong> {data_riunione}</li>
        <li><strong>Time:</strong> {ora_riunione}</li>
        <li><strong>Location:</strong> Meeting Room</li>
    </ul>
    <p>Please confirm your attendance by clicking one of the buttons below:</p>
    <a href="{mailto_conferma}" class="button">Confirm Attendance</a>
    <a href="{mailto_rifiuto}" class="button red">Cannot Attend</a>
    <p>Thank you!</p>
</body>
</html>
This template includes two buttons that link to mailto links for confirming or declining the meeting. The placeholders will be replaced with the actual date, time, and mailto links when the email is sent.

4. .gitignore
To ensure sensitive files are not included in version control, make sure to create a .gitignore file that excludes the .env and recipients.json files. Here’s an example of a .gitignore file:

```bash
# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 
# Recipients
recipients.json
```

## 4 - Usage
Once everything is configured, you can run the script using the CLI.

### 4.1 - Running the Script
To send an invitation email, use the following command:

```bash
python script_sender_email.py
```

This will prompt you for the event's date (--data) and time (--ora). The script will then send the email to all the recipients specified in the recipients.json file.

### 4.2 - CLI Options
- --data (-de): The date of the event (e.g., "30 January 2025").
- --ora (-o): The time of the event (e.g., "10:00").

Example
```bash
python script_sender_email.py --data "30 January 2025" --ora "10:00"
```
This will send an email invitation for the meeting scheduled on 30 January 2025 at 10:00 AM.

## 5 -Troubleshooting
- Authentication errors: Ensure that your email credentials in the .env file are correct. Some email providers may require enabling "less secure apps" or using an app-specific password.
- Missing recipients: Ensure that the recipients.json file is properly formatted and contains the correct email addresses.
- Email not sent: Check the SMTP server configuration in the .env file, and make sure your server supports SSL or TLS on the specified port.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## How to modify or add new features
- Change the template: You can modify the mailto_event_reminder.html file to change the design and content of the invitation email.
- Add recipients: To add new recipients, simply modify the recipients.json file and add the email addresses to the "destinatari" array.
- Modify SMTP settings: Change the SMTP server and port in the .env file if you're using a different email provider.