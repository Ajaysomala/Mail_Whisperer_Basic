# ui/app.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from email_reader.gmail_api import get_recent_emails
from filters.keyword_filter import is_important
from summary.summarizer import summarize_text
from tts.tts_engine import text_to_speech
from reports.daily_summary import generate_pdf_report
from utils.helpers import clean_html
import os

st.set_page_config(page_title="Mail Whisperer", layout="centered")

st.title("📬 Mail Whisperer")
st.markdown("Your private AI assistant for reading & summarizing emails.")

if st.button("📥 Fetch & Summarize Emails"):
    with st.spinner("Fetching emails..."):
        emails = get_recent_emails(limit=10)
        final_emails = []

        for idx, mail in enumerate(emails):
            if not is_important(mail):
                continue

            cleaned_body = clean_html(mail['body'])
            summary = summarize_text(cleaned_body)
            audio_path = text_to_speech(summary)

            mail["summary"] = summary
            mail["audio"] = audio_path
            final_emails.append(mail)

        if final_emails:
            st.success(f"✅ Found {len(final_emails)} important emails.")

            for idx, mail in enumerate(final_emails, 1):
                with st.expander(f"📩 Email {idx}: {mail['subject']}"):
                    st.markdown(f"**From:** {mail['from']}")
                    st.markdown(f"**Summary:** {mail['summary']}")

                    # Audio Playback
                    if os.path.exists(mail["audio"]):
                        audio_file = open(mail["audio"], "rb")
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format="audio/mp3")

            # Generate and offer PDF report
            pdf_path = generate_pdf_report(final_emails)
            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="📄 Download PDF Report",
                        data=f,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf"
                    )
        else:
            st.warning("No important emails found.")
