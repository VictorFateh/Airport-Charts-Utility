import os
import urllib.request

import requests
from bs4 import BeautifulSoup


def start_download(self, input_list, directory):
    for airport in input_list:
        iter_list = compile_diagram_list(airport)
        for i in iter_list:
            self.progress['maximum'] = len(iter_list)
            if download_file(directory, airport, i[0], i[1], i[2]):
                self.chart_text['text'] = i[1]
                self.airport_text['text'] = "Downloading: {}".format(airport.upper())
                self.progress.step()
    self.airport_text.destroy()
    self.chart_text.destroy()


def download_file(directory, airport, diagram_type, name, url):
    location = "{}/{}/{}/{}.pdf".format(directory, airport, diagram_type.strip(), name.replace('/', ''))
    try:
        path_to = "{}/{}/{}".format(directory, airport.upper(), diagram_type.strip().replace(" ", "+"))
        if not os.path.exists(path_to):
            os.makedirs(path_to)
        urllib.request.urlretrieve(url, location)
        return True
    except Exception as e:
        print("Unable to download {}".format(airport), e)
        os.rmdir("{}/{}".format(directory, airport))
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
