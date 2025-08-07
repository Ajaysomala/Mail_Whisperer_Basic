from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta

def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    text = soup.get_text(separator=' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def generate_summary():
    from email_reader.gmail_api import get_recent_emails as fetch_emails # Importing email fetch function
    emails = fetch_emails()

    # Define time range - past 24 hours
    now = datetime.now()
    cutoff_time = now - timedelta(hours=24)

    cleaned_bodies = []
    for email in emails:
        email_date = email.get('date')

        # If date is string, convert to datetime
        if isinstance(email_date, str):
            try:
                email_date = datetime.strptime(email_date, "%a, %d %b %Y %H:%M:%S %z")  # Modify this format if different
                email_date = email_date.replace(tzinfo=None)  # Make timezone naive for comparison
            except Exception:
                continue  # Skip if invalid date

        # Filter emails in last 24 hours
        if email_date and email_date >= cutoff_time:
            subject = email.get('subject', 'No Subject')
            sender = email.get('from', 'Unknown Sender')
            body = clean_html(email.get('body', ''))
            brief = f"Subject: {subject}. From: {sender}. Content: {body[:500]}..."
            cleaned_bodies.append(brief)

    if not cleaned_bodies:
        return "No recent emails found in the last 24 hours."

    final_summary = "\n\n".join(cleaned_bodies)
    return final_summary
