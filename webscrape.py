#Description: Scrape Inspirational Quotes Using Python

from bs4 import BeautifulSoup
import requests
import urllib.request
import random


#Create lists to store the scraped data
authors = []
quotes = []
combined_list = []


def get_quotes(page_number=0):
    """ Function to scrape the site """
    page_num = str(page_number)

    #append the page number to complete the URL
    URL = 'https://www.goodreads.com/quotes/tag/inspirational?page='+page_num

    try:
        webpage = requests.get(URL)
    except:
        print ("The URL was not found")

    #Parse the text from the website
    soup = BeautifulSoup(webpage.text, "html.parser")

    #Get the tag and it's class
    quoteText = soup.find_all('div', attrs={'class':'quoteText'})
    #print (quoteText)

    #Get the text of the current quote, but only the sentence before a new line
    for i in quoteText:
        quote = i.text.strip().split('\n')[0]
        author = i.find('span', attrs={'class':'authorOrTitle'}).text.strip()
        #print(quote)
        quotes.append(quote)
        #print(author)
        authors.append(author)

    #Combine the lists
    for i in range(len(quotes)):
        combined_list.append(quotes[i]+'-'+authors[i])

    #print (random.choice(combined_list))
    return combined_list



#Loop through 'n' pages
n = 1
for num in range(0,n):
  get_quotes(num)
