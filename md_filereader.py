import re
import markdown
from bs4 import BeautifulSoup

# Load markdown content
with open(r"C:\Users\shahi\Desktop\Security Training\scraped_output.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# Convert markdown to HTML
html = markdown.markdown(md_content)
soup = BeautifulSoup(html, 'html.parser')

# Extract raw text
text = soup.get_text()

# Regex patterns
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'(\+?\d{1,4}[-.\s]?)?(\(?\d{3}\)?[-.\s]?){1,2}\d{3,4}'
address_keywords = ['address', 'location', 'head office', 'office', 'HQ']

# Extract matches
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

# Extract possible address/location lines
address_lines = [line for line in text.split('\n') if any(kw.lower() in line.lower() for kw in address_keywords)]

# Output
print("\n📧 Emails found:", emails)
print("\n📞 Phone numbers found:", [''.join(p) for p in phones])
print("\n📍 Possible addresses/locations:")
for addr in address_lines:
    print("-", addr.strip())
