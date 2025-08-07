import os.path
import base64
import re
from email import message_from_bytes
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build 
from datetime import date



# If modifying, delete token.json
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def get_recent_emails(limit=5):
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=limit).execute()
    messages = results.get('messages', [])

    emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='raw').execute()
        raw = base64.urlsafe_b64decode(msg_data['raw'])
        email_msg = message_from_bytes(raw)

        subject = email_msg['Subject']
        sender = email_msg['From']
        body = extract_text_from_message(email_msg)

        emails.append({
            'subject': subject,
            'from': sender,
            'body': body,
            'date': date 
        })

    return emails

def extract_text_from_message(message):
    if message.is_multipart():
        for part in message.walk():
            ctype = part.get_content_type()
            if ctype == 'text/plain':
                return part.get_payload(decode=True).decode(errors='ignore')
    else:
        return message.get_payload(decode=True).decode(errors='ignore')
    return ""
