Web Scraper with Sitemap

This project is a Python-based web scraper that fetches URLs from a sitemap.xml file, scrapes text content from each page using Playwright, and saves the results into a Markdown file in the user's Downloads folder. Additionally, a second script is included to extract specific information (emails, phone numbers, and possible addresses) from the scraped Markdown output.

Features
- Fetches URLs from a specified sitemap.xml file.
- Scrapes visible text content from each page using headless Chromium via Playwright.
- Saves scraped data into a Markdown file with URLs as headings and content in blockquotes.
- Extracts emails, phone numbers, and possible address/location lines from the Markdown file using regex and keyword matching.
- Automatically saves the output to the system's Downloads folder.

Prerequisites
Before running the scripts, ensure you have the following installed:
- Python 3.7 or higher
- Required Python packages:
  - requests
  - playwright
  - asyncio
  - markdown
  - beautifulsoup4
  - re (built-in)

You can install the dependencies using pip:
pip install requests playwright markdown beautifulsoup4
playwright install  # Installs browser binaries for Playwright

Usage

Scraper Script
1. Set the Sitemap URL: Modify the `sitemap_url` variable in the scraper script to point to the target website's sitemap.xml file. For example:
   sitemap_url = "https://example.com/sitemap.xml"

2. Set the Output Filename: Adjust the `md_filename` variable to your desired output Markdown file name:
   md_filename = "scraped_output.md"

3. Run the Script: Execute the scraper script in a Python environment:
   python scraper.py

   The script will:
   - Fetch all URLs from the sitemap.
   - Scrape each page's text content.
   - Save the results to a Markdown file in your Downloads folder.

Data Extraction Script
1. Set the Input File Path: Update the file path in the extraction script to point to your scraped Markdown file:
   with open(r"C:\path\to\your\scraped_output.md", "r", encoding="utf-8") as f:

2. Run the Script: Execute the extraction script:
   python extractor.py

   The script will:
   - Convert the Markdown to HTML and extract raw text.
   - Use regex to find emails and phone numbers.
   - Search for lines containing address-related keywords.
   - Print the extracted information to the console.

Code Structure

Scraper Script
- fetch_sitemap_urls(sitemap_url): Retrieves all URLs from the provided sitemap.xml using the `requests` library and XML parsing with `xml.etree.ElementTree`.
- scrape_page_data(url, page): Asynchronously scrapes the visible text content of a webpage using Playwright.
- scrape_and_save_md(sitemap_url, md_filename): Orchestrates the scraping process and saves the results to a Markdown file.
- Main Execution: Uses `asyncio.run()` to handle the asynchronous operations.

Extraction Script
- Markdown to Text: Converts the Markdown file to HTML using `markdown`, then extracts raw text with `BeautifulSoup`.
- Regex Patterns:
  - Emails: Matches common email formats (e.g., `user@domain.com`).
  - Phone Numbers: Matches various phone number formats (e.g., `+123-456-7890`, `(123) 456-7890`).
  - Addresses: Searches for lines containing keywords like "address", "location", "office", etc.
- Output: Prints extracted emails, phone numbers, and potential address lines to the console.

Output

Scraper Output
The output Markdown file will be saved in your system's Downloads folder (e.g., ~/Downloads/scraped_output.md). It will have the following structure:
# Scraped Website Data

## [https://example.com/page1](https://example.com/page1)

> Page 1 content here
> More content...

## [https://example.com/page2](https://example.com/page2)

> Page 2 content here
> Additional text...

Extraction Output
The extraction script will print to the console:
📧 Emails found: ['user@example.com', 'contact@domain.org']

📞 Phone numbers found: ['+1234567890', '123-456-7890']

📍 Possible addresses/locations:
- Our office is located at 123 Main St, City, Country
- Contact us at our head office: 456 Elm St

Notes
- The scraper runs in headless mode (no browser UI) for efficiency.
- If a page fails to load or has no content, an error or warning will be printed, and the script will continue with the next URL.
- The extraction script assumes the Markdown file is well-formed and accessible at the specified path.
- Phone number and address detection may require fine-tuning of regex patterns or keywords based on the target website's content.

Limitations
- Requires an internet connection to fetch the sitemap and scrape pages.
- May not work with websites that heavily rely on JavaScript rendering beyond initial page load (additional wait strategies might be needed).
- Does not handle rate limiting or CAPTCHA challenges.
- The extraction script may miss some emails, phone numbers, or addresses if they don’t match the defined patterns or keywords.

License
This project is provided as-is for educational purposes. Feel free to modify and adapt it to your needs!
