from bs4 import BeautifulSoup as soup
from requests import get
import numpy as np

providers = dict()

url = 'https://clutch.co/au/agencies/digital-marketing?agency_size=2+-+9'
response = get(url)
html_soup = soup(response.text, 'html.parser')
# check how many pages
page_list = html_soup.find_all('li', class_ = "page-item last")                                                             
total_pages = int((page_list[0].contents[1])['data-page'])

url_list = list()

for pages in range(total_pages+2):
    if(pages == 0):
        nextpage = url
    else:
        nextpage = url + "&page="+str(pages)
    url_list.append(nextpage)


def get_data(url_source):
    response = get(url_source)
    html_soup = soup(response.text, 'html.parser')
    providersInThisPage =  html_soup.find_all('li', class_ = 'provider provider-row')
    
    #Get the fields container 
    # provider_list_on_this_page = list()
    for item in range(len(providersInThisPage)):
        company_name = (providersInThisPage[item].contents[1].findChild('h3').text).strip("\n")
        company_website = providersInThisPage[item].contents[1].find('a', class_ = "website-link__item", href = True)['href']
        providerDetails = (company_name, company_website)
        # print("Provider Name : ", providerDetails[0])
        # print("Website       : ", providerDetails[1], "\n")
        if (company_name in providers):
            pass
        else:
            # Write information to dictionary
            providers[company_name] = company_website
 
#  get_data(url_list[0])
#  harvest all data
for url in url_list:
    # print(url)
    get_data(url)

print(len(providers))

import csv
    
# field names  
fields = ['Provider Name', 'Website URL']  
csv_file = "providers.csv"
try:
    with open(csv_file, 'w', newline='') as csvfile:  
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)  
        # writing the fields  
        csvwriter.writerow(fields)
except IOError:
    print("I/O error")


# Saving Providers to CSV file
for items in providers.keys():
    rows = [ str(items), str(providers[items])] 
    # print(rows[0] + "    Website: " + rows[1])
    try:
        with open(csv_file, 'a', newline='') as csvfile:  
            # creating a csv writer object  
            writer = csv.writer(csvfile)
            writer.writerow(rows)
    except IOError:
        print("I/O error")
    