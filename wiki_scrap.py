import requests
from bs4 import BeautifulSoup
import pandas as pd

artists = pd.read_csv('unique_artists_for_scrape.csv')

results = []
error = []

limit = 20

for index, row in artists.iterrows():

    first_name = artists.loc[index,'Artist_First_Name']
    last_name = artists.loc[index,'Artist_Surname']

    #url = input('SENT FROM USER REQUEST')
    url = 'https://en.wikipedia.org/wiki/'+first_name + '_' + last_name
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    print('grabbing page for...' + first_name + last_name)

    try:
        header_artist_name = soup.find('h1', class_="firstHeading").text
        name_error = False
    except:
        header_artist_name = 'unfound' 
        name_error = True

    try: 
        artist_image_link = soup.find("a",{"class":"image"})
        image_error = False
    except:
        artist_image_link = 'unfound' 
        image_error = True
    
    try:
        artist_bio_paragraphs = (soup.find_all('p')[1].get_text())
        bio_error = False
    except:
        artist_bio_paragraphs = 'unfound'
        bio_error = True
    
    print('appending results...')
    results.append({
        'name' : (first_name, last_name),
        'header' : header_artist_name,
        'image':artist_image_link,
        'bio':artist_bio_paragraphs
    })

    if name_error == True or image_error == True or bio_error == True:
        error.append({
        'name' : (first_name, last_name),
        'header error' : name_error,
        'image error': image_error,
        'bio error': bio_error
    })
    print('Moving onto next row...')

print('done with scrapping, exporting to csv...')
artist_scraping_table = pd.DataFrame(results)
artist_scraping_table.to_csv('artist_scrape_results.csv')

artist_scrapping_errors_table = pd.DataFrame(error)
artist_scrapping_errors_table.to_csv('scraping_errors.csv')


    #table = soup.find_all('div', class_="mw-parser-output").contents
    #print(table)
