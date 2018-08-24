from bs4 import BeautifulSoup
import requests
import sys
import os


def main():
    airpot_list = open("airports.txt", "r").read().split('\n')

    test_list = ["KPDX", "KSFO", "KPAO"]
    for airport in test_list:
        chart_download(airport)


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
        if "STARs" in STARS_HEADER.text:
            if not os.path.exists("Charts/{}/{}".format(airport, STARS_HEADER.text)):
                os.makedirs("Charts/{}/{}".format(airport, STARS_HEADER.text))
            APPROACH_HEADER = STARS_HEADER.findNext('th')
            if "IAPs" in APPROACH_HEADER.text:
                if not os.path.exists("Charts/{}/{}".format(airport, APPROACH_HEADER.text)):
                    os.makedirs("Charts/{}/{}".format(airport, APPROACH_HEADER.text))
                DEPARTURE_HEADER = APPROACH_HEADER.findNext('th')
                if "Departure" in DEPARTURE_HEADER.text:
                    if not os.path.exists("Charts/{}/{}".format(airport, DEPARTURE_HEADER.text)):
                        os.makedirs("Charts/{}/{}".format(airport, DEPARTURE_HEADER.text))

        print(STARS_HEADER.text + "\n" + APPROACH_HEADER.text + "\n" + DEPARTURE_HEADER.text)

    except:
        print("Error", sys.exc_info())
        pass


if __name__ == '__main__':
    main()
