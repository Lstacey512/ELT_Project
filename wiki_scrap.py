import requests
from bs4 import BeautifulSoup
import pandas as pd

artists = pd.read_csv('unique_artists_for_scrape.csv')

for index, row in artists.iterrows():

    first_name = artists.loc[index,'Artist_First_Name']
    last_name = artists.loc[index,'Artist_Surname']

    #url = input('SENT FROM USER REQUEST')
    url = 'https://en.wikipedia.org/wiki/'+ first_name + '_' + last_name
    print(url)
    #page = requests.get(url)

    #soup = BeautifulSoup(page.text, 'html.parser')

    #print(soup.prettify())

    #print artist name for header
    #header_artist_name = soup.find('h1', class_="firstHeading").text
    #print(header_artist_name)

    #print link to image of artist
    #artist_image_link = soup.find("a",{"class":"image"})
    #print (artist_image_link["href"])

    #print artist first paragraph of bio
    #artist_bio_paragraphs = (soup.find_all('p')[1].get_text())
    #print(artist_bio_paragraphs)


    #table = soup.find_all('div', class_="mw-parser-output").contents
    #print(table)
