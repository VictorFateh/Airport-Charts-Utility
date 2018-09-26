import os
import sys
import urllib.request

import requests
from bs4 import BeautifulSoup


def start_download(input_list):
    for airport in input_list:
        for i in scrape_page(airport):
            download_file(airport, i[0], i[1])


def download_file(airport, name, url):
    if not os.path.exists("Charts/{}".format(airport)):
        os.makedirs("Charts/{}".format(airport))
    location = "Charts/{}/{}.pdf".format(airport, name.replace('/', ''))
    urllib.request.urlretrieve(url, location)


# Given an airport ICAO, returns list
# [("APPROACH NAME", "PDF URL"), ("...", "..."), ...]
def scrape_page(airport):
    try:
        data = requests.get("https://www.airnav.com/airport/{}".format(airport))

        soup = BeautifulSoup(data.text, 'html.parser')

        pdf_list = []

        pdf_table = soup.find(text="Instrument Procedures").parent.findNext('table')

        for link in pdf_table.find_all('a'):
            title_pdf_tuple = (link.findPrevious('td').findPrevious('td').findPrevious('td').text, link['href'][8:])
            pdf_list.append(title_pdf_tuple)

        return pdf_list

    except Exception as e:
        return "Error: ", e


if __name__ == "__main__":
    test_list = ['KSJC', 'KSFO', 'KPAO']
    start_download(test_list)
