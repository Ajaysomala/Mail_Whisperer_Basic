# filters/keyword_filter.py

IMPORTANT_KEYWORDS = [
    "invoice", "payment", "due", "meeting", "reminder", "schedule", "interview",
    "report", "project", "client", "deadline", "follow-up"
]

def is_important(email_dict):
    subject = email_dict.get("subject", "").lower()
    body = email_dict.get("body", "").lower()

    for keyword in IMPORTANT_KEYWORDS:
        if keyword in subject or keyword in body:
            return True
    return False
 