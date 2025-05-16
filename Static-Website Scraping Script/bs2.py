import requests  # Import the requests library to fetch webpage content
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML

# Define the target webpage URL
url = "https://www.securityconcepts.ca/about.html"

# Send an HTTP GET request to fetch the webpage
response = requests.get(url)

# Check if the request was successful (status code 200 means OK)
if response.status_code == 200:
   
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the page title (if available), otherwise set a default message
    title = soup.title.text if soup.title else "No Title Found"
    
    # Extract all headings (h1 tags) and store them in a list
    headings = [h.text for h in soup.find_all('h1')]
    
    # Extract all paragraph (p tags) content and store them in a list
    paragraphs = [p.text for p in soup.find_all('p')]
    
    # Print the extracted title
    print(f"Title: {title}\n")
    
    # Print all extracted headings
    print("Headings:")
    for heading in headings:
        print(f"- {heading}")
    
    # Print up to 100 paragraphs to avoid excessive output
    print("\nParagraphs:")
    for para in paragraphs[:100]:  
        print(f"- {para}\n")

# Handle the case when the request fails
else:
    print(f"Failed to retrieve page, status code: {response.status_code}")
