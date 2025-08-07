# reports/daily_summary.py

from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_pdf_report(emails, filename=None):
    from pathlib import Path
    if not filename:
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"daily_summary_{today}.pdf"

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)  # ✅ Ensure folder exists
    filepath = reports_dir / filename

    c = canvas.Canvas(str(filepath), pagesize=LETTER)

    width, height = LETTER
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Mail Whisperer: Daily Summary Report")
    y -= 40

    c.setFont("Helvetica", 12)
    for idx, mail in enumerate(emails):
        summary = mail.get('summary', '[No summary found]')  # ✅ Avoid KeyError
        c.drawString(50, y, f"Email {idx+1}")
        y -= 20
        c.drawString(60, y, f"From: {mail.get('from', 'Unknown')}")
        y -= 20
        c.drawString(60, y, f"Subject: {mail.get('subject', 'No Subject')}")
        y -= 20
        c.drawString(60, y, "Summary:")
        y -= 20

        lines = summary.split(". ")
        for line in lines:
            if y < 100:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 12)
            c.drawString(70, y, f"- {line.strip()}")
            y -= 20

        y -= 10

    c.save()
    return str(filepath)
