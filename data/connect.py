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
            img = r.select("img")
            # print(first, last)
            # print(team)
            # print(country)
            # print(img)
            drivers.append([first, last, team, country])

        return drivers
    
    def get_driver(self, name):
        soup = self.connect("/drivers/" + name)
        selector = r"#statistics > div > div > div > div > div.order-1 > div  dl > div"
        tags = soup.select(selector)

        result_list = []
        for info_div in tags:
            title_tag = info_div.select_one('dt')
            value_tag = info_div.select_one('dd')
            title = title_tag.text
            value = value_tag.text
            result_list.append([title, value])

        print(result_list)

        return result_list

    def get_driver_career(self, name):
        soup = self.connect("/drivers/" + name)
        data = soup.select('#statistics > div > div > div > div > div.order-3 > div > dl > div')

        datalist = []
        for i in data:
            temp = []
            temp.append(i.select_one('.DataGrid-module_title__hXN-n').text)
            temp.append(i.select_one('.DataGrid-module_description__e-Mnw').text)
            datalist.append(temp)

        print(datalist)

    def get_drivers_dict(self):
        soup = self.connect("/drivers")
        result = soup.select("#maincontent > div > div > div > div > div.grid.grid-cols-1.\@\[680px\]\/page\:grid-cols-2.\@\[1660px\]\/page\:grid-cols-4.gap-px-16.lg\:gap-px-24 > div > a > div")
        print(result[0].prettify()[0:100])

        drivers = []

        for r in result:
            last = r.select("div.z-10.min-h-\[112px\].text-static-static-1 > p.typography-module_display-l-regular__MOZq8.group-hover\/driver-card\:underline")[0].text
            first = r.select("div.z-10.min-h-\[112px\].text-static-static-1 > p.typography-module_display-l-bold__m1yaJ.group-hover\/driver-card\:underline")[0].text
            team = r.select("div.z-10.min-h-\[112px\].text-static-static-1 > div.pt-px-4.pb-px-16")[0].text
            country = r.select("svg")[0].text
            name = f'{first} {last}'.strip()

            driver_dict = {
                'name': name,
                'team': team,
                'country': country
            }    
            drivers.append(driver_dict)
        return drivers
