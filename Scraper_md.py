import asyncio
import requests
import xml.etree.ElementTree as ET
import os
from pathlib import Path
from playwright.async_api import async_playwright

# Get the system's Downloads folder
DOWNLOADS_FOLDER = str(Path.home() / "Downloads")

# Fetch URLs from sitemap.xml
def fetch_sitemap_urls(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch sitemap: {response.status_code}")
    
    root = ET.fromstring(response.text)
    urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    return urls

# Scrape text content from a page
async def scrape_page_data(url, page):
    try:
        print(f"Visiting: {url}")
        await page.goto(url, wait_until="load")  # Ensure full page load
        await page.wait_for_selector("body", state="attached")  # Ensure body is loaded

        # Extract visible text
        content = await page.inner_text("body")

        if not content.strip():
            print(f"Warning: No content found for {url}")
        
        return content
    
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

# Scrape multiple pages and save data to a Markdown file
async def scrape_and_save_md(sitemap_url, md_filename):
    urls = fetch_sitemap_urls(sitemap_url)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        md_content = "# Scraped Website Data\n\n"
        
        for url in urls:
            print(f"Scraping: {url}")
            content = await scrape_page_data(url, page)
            
            if content.strip():  # Only save if content is extracted
                md_content += f"## [{url}]({url})\n\n"
                md_content += f"> {content.replace('\n', '\n> ')}\n\n"  # Blockquote for better readability
        
        await browser.close()

        # Save file to Downloads folder
        output_path = os.path.join(DOWNLOADS_FOLDER, md_filename)
        with open(output_path, mode='w', encoding='utf-8') as file:
            file.write(md_content)
        
        print(f"Data saved to {output_path}")

# Example usage
sitemap_url = "https://www.securitas.ca/sitemap.xml"  # Change this to the target sitemap
md_filename = "scraped_output.md"

asyncio.run(scrape_and_save_md(sitemap_url, md_filename))
