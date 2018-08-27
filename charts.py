import os
import sys
import urllib.request

import requests
from bs4 import BeautifulSoup


def start_download(input_list):
    for airport in input_list:
        chart_download(airport)


def chart_downloader(url, airport, section, name):
    r = requests.get(url)
    cur = os.path.dirname(os.path.realpath(__file__))
    directory = "\Charts\%s\%s\%s.pdf" % (airport, section, name)
    print(cur + directory)
    urllib.request.urlretrieve(url, directory)


# Given an airpot ICAO code, download all charts
# https://www.airnav.com/airport/{airport}
def chart_download(airport):
    try:
        raw_html = requests.get("https://www.airnav.com/airport/{}".format(airport)).text

        if not os.path.exists("Charts/{}".format(airport)):
            os.makedirs("Charts/{}".format(airport))

        soup = BeautifulSoup(raw_html, features="html.parser")

        insert = soup.find(text="Instrument Procedures")

        STARS_HEADER = insert.parent.findNext('th')
        APPROACH_HEADER = STARS_HEADER.findNext('th')
        DEPARTURE_HEADER = APPROACH_HEADER.findNext('th')

        star_str = STARS_HEADER.text.lstrip()
        app_str = APPROACH_HEADER.text.lstrip()
        dep_str = DEPARTURE_HEADER.text.lstrip()

        if "STARs" in star_str:
            if not os.path.exists("Charts/{}/{}".format(airport, star_str)):
                os.makedirs("Charts/{}/{}".format(airport, star_str))
            if "IAPs" in app_str:
                if not os.path.exists("Charts/{}/{}".format(airport, app_str)):
                    os.makedirs("Charts/{}/{}".format(airport, app_str))
                if "Departure" in dep_str:
                    if not os.path.exists("Charts/{}/{}".format(airport, dep_str)):
                        os.makedirs("Charts/{}/{}".format(airport, dep_str))

        print(star_str + "\n" + app_str + "\n" + dep_str)

    except:
        print("Error", sys.exc_info())
        pass
