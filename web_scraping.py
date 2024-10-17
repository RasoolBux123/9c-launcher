import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example.com"  # Replace with the target website

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles (this will depend on the site's structure)
titles = soup.find_all('h2', class_='title')  # Example: Replace with actual tags and class names

# Loop through the titles and print them
for index, title in enumerate(titles, start=1):
    print(f"{index}. {title.get_text()}")

