import json
import requests
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features
from selenium import webdriver
from operator import attrgetter

def watson_sentiments(url_news):

    natural_language_understanding = NaturalLanguageUnderstandingV1(
      username="57e4c1cb-5089-42da-b29a-ef0fc6a597dc",
      password="BxcDxa7qkhh0",
      version="2017-02-27")

    response = natural_language_understanding.analyze(
      url=url_news,
      features=[
        Features.Entities(
          # Entities options
          sentiment=True,
          limit=1
        )
      ]
    )

    return response


class Entry:
    def __init__(self, entity, sentiment, url):
        self.entity = entity
        self.sentiment = sentiment
        self.url = url

def getPageUrl(elementLinks):
    extractLinks = []
    for element in elementLinks:
        links = element.get_attribute('href')
        extractLinks.append(links)
    return(extractLinks)

def getUrls():
    browser = webdriver.Chrome()
    browser.get('http://finance.google.com/')
    ## Extract all article urls
    articleLinks = []
    elementLinks = browser.find_elements_by_id('n-hp-')
    links = getPageUrl(elementLinks)
    articleLinks.append(links)

    articleLinks = [y for x in articleLinks for y in x]
    print(articleLinks)
    urls = []
    for link in articleLinks:
        r = requests.get(link)
        # browser.get(link)
        # time.sleep(0.2)
        # link = browser.current_url
        urls.append(r.url)

    print(urls)
    return urls

##TO DO(1) load list_urls
urls = getUrls()
print(len(urls))
# loads the list of responses, unprocessed
entities = []
sentiments = []
for link in urls:
    response = watson_sentiments(link)
    print(response)
    res = response['entities'][0]
    if res is not None:
        entities.append(res['text'])
        sentiments.append(res['sentiment']['score'])

entries = []
entries_sorted = []
for i in range(len(entities)):
    entry = Entry(entities[i], sentiments[i],urls[i])
    entries.append(entry)

## TO DO(3) sort list_entries in decending order of sentiments
entries_sorted = sorted(entries, key=attrgetter('sentiment'), reverse=True)
for entry in entries_sorted:
    print(entry.entity, entry.sentiment, entry.url)

## TO DO(4) Format the sorted list_entries





       
        


    
##print(watson_sentiments('cnn.com'))




##entry_1 = entry('cnn.com')


##print(json.dumps(response, indent=2))

