import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage containing the links
url = "https://www.ndbc.noaa.gov/data/realtime2/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all anchor tags ( <a> ) which contain links
links = soup.find_all("a", href=True)

# Extract and filter links ending with .txt
txt_links = [link["href"] for link in links if link["href"].endswith(".txt")]

# The links are relative URLs, so prepend the base URL to make them complete
complete_links = [url + link for link in txt_links]

# Print the complete links to .txt files
for link in complete_links:
    print(link)

