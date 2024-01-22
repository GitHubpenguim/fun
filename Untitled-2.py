
import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.content, 'html.parser')

## Find All Quotes
print(soup.find_all('span', class_='text'))

"""
Output:

[
    <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>,
    <span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>,
    <span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>,
    ...
]

"""
