'''
작성자: 김가람
날짜: 2025-10-22
'''
import requests
from bs4 import BeautifulSoup

class WebConnectManager:
    url = "https://www.formula1.com/en"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    
    def __init__(self):
        pass
        
    def connect(self, path):
        # 요청
        res = requests.get(self.url + path, headers={"user-agent":self.user_agent})

        if res.status_code == 200:
            return BeautifulSoup(res.text, "lxml")
        else:
            print("응답을 받지 못함.", res.status_code)
            return None 

    def get_drivers(self):
        soup = self.connect("/drivers")
        result = soup.select("#maincontent > div > div > div > div > div.grid.grid-cols-1.\@\[680px\]\/page\:grid-cols-2.\@\[1660px\]\/page\:grid-cols-4.gap-px-16.lg\:gap-px-24 > div > a > div")
        print(result[0].prettify()[0:100])

        drivers = []

        for r in result:
            last = r.select_one("div.z-10.min-h-\[112px\].text-static-static-1 > p.typography-module_display-l-regular__MOZq8.group-hover\/driver-card\:underline").text
            first = r.select_one("div.z-10.min-h-\[112px\].text-static-static-1 > p.typography-module_display-l-bold__m1yaJ.group-hover\/driver-card\:underline").text
            team = r.select_one("div.z-10.min-h-\[112px\].text-static-static-1 > div.pt-px-4.pb-px-16").text
            country = r.select_one("svg").text
            img = r.select_one("img").attrs["src"]

            name = f'{last} {first}'.strip()
            
            driver_dict = {
                'name': name,
                'team': team,
                'country': country,
                'image_url': img
            }    
            drivers.append(driver_dict)

        return drivers
    
    def get_driver(self, name) -> dict:
        path_name = name.lower().replace(" ", "-")

        soup = self.connect("/drivers/" + path_name)
        selector = r"#statistics > div > div > div > div > div.order-1 > div  dl > div"
        tags = soup.select(selector)

        dict = {"name": name}

        for info_div in tags:
            title_tag = info_div.select_one('dt')
            value_tag = info_div.select_one('dd')
            title: str = title_tag.text.lower().replace(" ", "_")
            value: str = value_tag.text

            if "st" in value or "th"in value or "nd"in value or "rd"in value:
                value = value.replace("st", "")
                value = value.replace("th", "")
                value = value.replace("nd", "")
                value = value.replace("rd", "")

            print(title, value)

            dict[title] = value

        return dict

    def get_driver_career(self, name) -> dict:
        path_name = name.lower().replace(" ", "-")
        
        soup = self.connect("/drivers/" + path_name)
        data = soup.select('#statistics > div > div > div > div > div.order-3 > div > dl > div')

        dict = {"name": name}

        for i in data:
            temp = []
            title_text: str = i.select_one('.DataGrid-module_title__hXN-n').text
            title: str = title_text.lower().replace(" ", "_")
            value: str = i.select_one('.DataGrid-module_description__e-Mnw').text

            if " " in value:
                value = value.split(" ")[0]

            dict[title] = value

        return dict
