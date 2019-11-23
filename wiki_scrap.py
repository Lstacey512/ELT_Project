import requests
from bs4 import BeautifulSoup
import pandas as pd

artists = pd.read_csv('artists_table.csv')

results = []
error = []

limit = 20

for index, row in artists.iterrows():

    name = artists.loc[index,'Full_name']

    #url = input('SENT FROM USER REQUEST')
    url = 'https://en.wikipedia.org/wiki/'+ name
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    print('grabbing page for...' + name)

    try:
        header_artist_name = soup.find('h1', class_="firstHeading").text
        name_error = False
    except:
        header_artist_name = 'unfound' 
        name_error = True

    try: 
        artist_image_search = soup.find("a",{"class":"image"})
        artist_image_link = artist_image_search["href"]
        image_error = False
    except:
        artist_image_link = 'unfound' 
        image_error = True
    
    try:
        artist_bio_first_para = soup.find_all("p", class_="mw-parser-output")
        whitelist = [
                     'p'
                        ]

        p_elements = [t for t in soup.find_all() if t.name in whitelist]

        artist_bio_paragraphs = [t.get_text() for t in p_elements if "b" == list(t.children)[0].name]
        #print(p_we_want)
        bio_error = False
        
    except:
        artist_bio_paragraphs = 'unfound'
        bio_error = True
    
    print('appending results...')
    results.append({
        'name' : (name),
        'header' : header_artist_name,
        'image':artist_image_link,
        'bio':artist_bio_paragraphs
    })

    if name_error == True or image_error == True or bio_error == True:
        error.append({
        'name' : (name),
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
