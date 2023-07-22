import requests
from bs4 import BeautifulSoup

# URL to the website you want to scrape
url = 'https://example.com'

# Send an HTTP request to the URL and get the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract specific data elements based on HTML tags and classes
data_elements = soup.select('div.content > p')

# Process and display the scraped data
for element in data_elements:
    print(element.get_text())

# You can further manipulate the data, save it to a file, or perform data analysis as needed.
