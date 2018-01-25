import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


def scrape():
    mars_data = {
        'news_title':'Steep Slopes on Mars Reveal Structure of Buried Ice',
        'news_p':"Researchers using NASA's Mars Reconnaissance Orbiter have found eight sites where thick deposits of ice beneath Mars' surface are exposed.",
        'featured_image_url':'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA19347_ip.jpg',
        'mars_weather': 'party sunny with a high of 20',
        'hemisphere_image_urls': [{'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',
          'title': 'Cerberus Hemisphere Enhanced'},
         {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',
          'title': 'Schiaparelli Hemisphere Enhanced'},
         {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',
          'title': 'Syrtis Major Hemisphere Enhanced'},
         {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',
          'title': 'Valles Marineris Hemisphere Enhanced'}]


    }

    return mars_data


if __name__ == "__main__":
    scrape()

# print(mars_data['news_title'])
# print(mars_data['hemisphere_image_urls'][0]['img_url'])
#
# [print(i['img_url']) for i in mars_data['hemisphere_image_urls']]
