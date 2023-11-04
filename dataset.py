import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

# URL:
url = "https://www.ndbc.noaa.gov/data/realtime2/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

links = soup.find_all("a", href=True)

txt_links = [link["href"] for link in links if link["href"].endswith(".txt")]
complete_links = [url + link for link in txt_links]

# Print the complete links to .txt files
for link in complete_links:
    print(link)
