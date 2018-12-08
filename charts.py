import os
import urllib.request

import requests
from bs4 import BeautifulSoup


def start_download(input_list, directory):
    for airport in input_list:
        for i in scrape_flightaware(airport):
            if download_file(directory, airport, i[0], i[1], i[2]):
                print("{} - {} downloaded".format(airport, i[1]))


def download_file(directory, airport, diagram_type, name, url):
    location = "{}/{}/{}/{}.pdf".format(directory, airport, diagram_type.strip(), name.replace('/', ''))
    try:
        if not os.path.exists("{}/{}/{}".format(directory, airport, diagram_type)):
            os.makedirs("{}/{}/{}".format(directory, airport, diagram_type.strip().replace(" ", "+")))
        urllib.request.urlretrieve(url, location)
        return True
    except Exception as e:
        print("Unable to download {}".format(airport), e)
        os.rmdir("{}/{}".format(directory, airport))
        return False


# Diagram: https://flightaware.com/resources/airport/SFO/APD/AIRPORT+DIAGRAM/pdf
# Procedures: https://flightaware.com/resources/airport/KSFO/procedures
# Returns list ready to download [TYPE, NAME, PDF_URL]
def scrape_flightaware(airport):
    try:
        data = requests.get("https://flightaware.com/resources/airport/{}/procedures".format(airport))

        soup = BeautifulSoup(data.text, 'html.parser')

        pdf_list = []

        data_row = soup.find_all('div', {'class': 'row'})[2]

        for table in data_row.find_all('table'):
            for link in table.find_all('a'):
                download_info = (link.parent.findPrevious('td').getText(), link.get_text(),
                                 "https://flightaware.com/resources/{}/pdf".format(link['href'][11:]))
                pdf_list.append(download_info)

        return pdf_list

    except Exception as e:
        return "Error: ", e
