# utils/helpers.py

from bs4 import BeautifulSoup
import re

def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    text = soup.get_text(separator=' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text
