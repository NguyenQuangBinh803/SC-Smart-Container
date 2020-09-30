#  Copyright (C) AI Power - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Edward J. C. Ashenbert - Miyuki Nogizaka, September 2020

import lxml.html as lh
import requests

class ContainerInformationRequest:

    def __init__(self, owner_code, serial_number=""):
        self.owner_code = owner_code
        self.url = "https://www.bic-code.org/container-bic-code/" + self.owner_code + "/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.owner_information = dict.fromkeys(['Company','Code','Address','Zip Code','City','State','Country','Telephone','Fax','BoxTech','Web'])

    def set_owner_code(self, owner_code):
        self.owner_code = owner_code
        self.url = "https://www.bic-code.org/container-bic-code/" + self.owner_code + "/"

    def request_information(self):
        page = requests.get(self.url, headers=self.headers)
        doc = lh.fromstring(page.content)
        tr_elements = doc.xpath('//tbody')

        th_elemnet = tr_elements[0][0].xpath("//th")
        td_element = tr_elements[0][0].xpath("//td")

        for index, element in enumerate(td_element):
            feild = th_elemnet[index].text_content()
            name = td_element[index].text_content()
            self.owner_information[feild] = name

        return self.owner_information

if __name__ == "__main__":
    request_information = ContainerInformationRequest("KKFU")
    print(request_information.request_information())
