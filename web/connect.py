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

    def connect(self, path, selector):
        # 요청
        
        res = requests.get(self.url + path, headers={"user-agent":self.user_agent})

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "lxml")
            result = soup.select(selector)
            print(result[0].prettify()[0:100])

            return result
        else:
            print("응답을 받지 못함.", res.status_code)
            return None 

    def get_drivers(self):
        result = self.connect("/drivers", "#maincontent > div > div > div > div > div.grid.grid-cols-1.\@\[680px\]\/page\:grid-cols-2.\@\[1660px\]\/page\:grid-cols-4.gap-px-16.lg\:gap-px-24 > div > a > div")
        
        drivers = []

        for r in result:
            last = r.select("div.z-10.min-h-\[112px\].text-static-static-1 > p.typography-module_display-l-regular__MOZq8.group-hover\/driver-card\:underline")[0].text
            first = r.select("div.z-10.min-h-\[112px\].text-static-static-1 > p.typography-module_display-l-bold__m1yaJ.group-hover\/driver-card\:underline")[0].text
            team = r.select("div.z-10.min-h-\[112px\].text-static-static-1 > div.pt-px-4.pb-px-16")[0].text
            country = r.select("svg")[0].text
            img = r.select("img")
            print(first, last)
            print(team)
            print(country)
            print(img)
            drivers.append((first, last, team, country))

        return drivers
