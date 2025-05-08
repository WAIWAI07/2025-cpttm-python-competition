# Today news

# Ask the user for the keywords
# And find the news that the title contains the keywords

import requests
import bs4
import datetime

# Get today year
year = datetime.datetime.now().year

# Get today month
month = datetime.datetime.now().month

# Get today day
day = datetime.datetime.now().day

# Merge in the macaodaily url
url = f"http://macaodaily.com/html/{year}-{month:02d}/{day:02d}/node_1.htm"


# Get the html content
html = requests.get(url)
html.encoding = "utf-8"

# Parse the html content
soup = bs4.BeautifulSoup(html.text, "html.parser")

# Get all a tags
a_tags: list[bs4.element.Tag] = soup.find_all("a")

# Get user input
keywords = [i.strip() for i in input("Enter keywords: ").split(",")]

# Print all a tags
for a_tag in a_tags:
    for keyword in keywords:
        if keyword in a_tag.text:
            break
    else:
        continue

    news_title = a_tag.text

    news_url = f"http://macaodaily.com/html/{year}-{month:02d}/{day:02d}/{a_tag.attrs['href']}"

    news_html = requests.get(news_url)
    news_html.encoding = "utf-8"

    news_soup = bs4.BeautifulSoup(news_html.text, "html.parser")

    news_content = '\n'.join([i.text.rstrip() for i in news_soup.find_all("p") if i.text])

    print(news_title)

    print(news_content)
    
    print("-" * 50)