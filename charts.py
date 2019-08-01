import os
import urllib.request

import requests
from bs4 import BeautifulSoup


def start_download(self, input_list):
    for airport in input_list:
        for i in compile_diagram_list(airport):
            self.progress['maximum'] = len(compile_diagram_list(airport))
            if download_file(airport, i[0], i[1], i[2]):
                self.progress.step()
                self.airport_text['text'] = "Downloading: {}".format(airport.upper())
                self.chart_text['text'] = i[1]



def download_file(airport, diagram_type, name, url):
    location = "Charts/{}/{}/{}.pdf".format(airport, diagram_type, name.replace('/', ''))
    try:
        if not os.path.exists("Charts/{}/{}".format(airport, diagram_type)):
            os.makedirs("Charts/{}/{}".format(airport, diagram_type))
        urllib.request.urlretrieve(url, location)
        return True
    except Exception as e:
        print("Unable to download {}".format(airport), e)
        os.rmdir("Charts/{}".format(airport))
        return False


# URL Example: https://flightaware.com/resources/airport/SFO/APD/AIRPORT+DIAGRAM/pdf
# Returns list ready to download [TYPE, NAME, PDF_URL]
def compile_diagram_list(airport):
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
