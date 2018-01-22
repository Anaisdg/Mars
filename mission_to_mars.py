
# coding: utf-8

# # Example:
# news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
# 
# news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."

# # Scrapping With Pandas

# In[90]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup


# In[21]:


browser = Browser('chrome', headless=False)
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[22]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[38]:


content_title = soup.find('div', class_='content_title').find('a')


# In[39]:


content_title


# In[40]:


news_title = content_title.text.strip()


# In[41]:


news_title


# In[42]:


article_teaser_body = soup.find('div', class_='article_teaser_body')


# In[43]:


article_teaser_body


# In[44]:


news_p=article_teaser_body.text.strip()


# In[45]:


news_p


# In[117]:


browser = Browser('chrome', headless=False)
url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)


# In[84]:


baseurl = 'https://www.jpl.nasa.gov'


# In[49]:


html2 = browser.html
soup2 = BeautifulSoup(html2, 'html.parser')


# In[118]:


button = soup2.find('a', class_='button fancybox')
button


# In[82]:


image_url = soup2.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')
image_url


# In[87]:


featured_image_url = baseurl + image_url
featured_image_url


# In[180]:


browser = Browser('chrome', headless=False)
url3 = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url3)


# In[181]:


html3 = browser.html
soup3 = BeautifulSoup(html3, 'html.parser')


# In[182]:


tweet = soup3.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')


# In[184]:


mars_weather = tweet.text.strip()
mars_weather


# In[199]:


url4 = 'https://space-facts.com/mars/'


# In[200]:


tables = pd.read_html(url4)


# In[201]:


tables


# In[202]:


df = tables[0]
df.head()


# In[204]:


print(df.to_html())


# In[205]:


browser = Browser('chrome', headless=False)
url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url5)


# In[208]:


html5 = browser.html
soup5 = BeautifulSoup(html5, 'html.parser')


# In[207]:


one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'


# In[226]:


links = [one, two, three, four]


# In[224]:


a = soup5.find_all('h3')
a


# In[227]:


descriptions = [h3.text.strip() for h3 in a]
descriptions


# In[236]:


hemisphere_image_urls = [{'title': description, 'img_url': link} for description, link in zip(descriptions,links)]


# In[237]:


hemisphere_image_urls

