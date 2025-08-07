from email_reader.gmail_api import get_recent_emails
from filters.keyword_filter import is_important
from summary.summarizer import summarize_text 
from tts.tts_engine import text_to_speech
from reports.daily_summary import generate_pdf_report
from utils.helpers import clean_html  # ✅ import cleaner

def main():
    print("Fetching recent emails...\n")
    emails = get_recent_emails(limit=10)

    final_emails = []

    for idx, mail in enumerate(emails):
        if not is_important(mail):
            continue

        print(f"\n📩 Important Email {idx+1}")
        print(f"From: {mail['from']}")
        print(f"Subject: {mail['subject']}")

        # ✅ Clean HTML before summarizing
        cleaned_body = clean_html(mail['body'])
        summary = summarize_text(cleaned_body)

        print(f"Summary:\n{summary}\n")

        # 🗣️ Generate TTS
        audio_path = text_to_speech(summary)
        print(f"🗣️  Audio saved at: {audio_path}")

        # Store for PDF
        mail["summary"] = summary
        final_emails.append(mail)

    # Generate PDF report if emails found
    print(f"\n📦 Total important emails processed: {len(final_emails)}")

    if final_emails:
        try:
            pdf_path = generate_pdf_report(final_emails)
            print(f"\n📄 PDF report saved at: {pdf_path}")
        except Exception as e:
            print(f"❌ Error generating PDF: {e}")
    else:
        print("⚠️ No important emails to include in the report.")


if __name__ == '__main__':
    main()
