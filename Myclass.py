import pandas as pd
import numpy as np
import requests
from selenium import webdriver
from bs4 import BeautifulSoup


class Sport:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome('C:/Users/Eugene/Downloads/chromedriver.exe')
        self.elements = ''
        self.file = ''

    def start(self):
        self.driver.get(self.url)
        self.elements = self.driver.find_elements_by_class_name("wikitable")

    def parsing(self, file):
        self.file = open(file, "r")
        return self.file.read()


class Myclass(Sport):

    def __init__(self):
        super().__init__('https://www.fonbet.ru/#!/')
        self.element = ''
        self.file = ''

    def start(self):
        self.driver.get(self.url)
        self.element = self.driver.find_element_by_class_name("home__line").get_attribute('innerHTML')

        with open('test.txt', 'w') as output:
            output.write(self.element)

    def parsing(self, file):
        return super().parsing(file)

    def get_post(self):
        return requests.post(self.url).text

    def get_responce(self):
        return requests.get(self.url).json()


class JuniorDosSantos(Sport):
    def __init__(self):
        super().__init__('https://ru.wikipedia.org/wiki/%D0%94%D1%83%D1%81_%D0%A1%D0%B0%D0%BD%D1%82%D1%83%D1%81,_%D0%96%D1%83%D0%BD%D0%B8%D0%BE%D1%80')

    def start(self):

        super().start()
        element = self.elements[1].get_attribute('innerHTML')
        with open('Junior Dos Santos.txt', 'w') as output:
            output.write(element)

    def parsing(self, file='Junior Dos Santos.txt'):
        return super().parsing(file)


class CainVelasquez(Sport):
    def __init__(self):
        super().__init__('https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D0%BB%D0%B0%D1%81%D0%BA%D0%B5%D1%81,_%D0%9A%D0%B5%D0%B9%D0%BD')

    def start(self):

        super().start()
        element = self.elements[1].get_attribute('innerHTML')
        with open('Cain Velasquez.txt', 'w') as output:
            output.write(element)

    def parsing(self, file='Cain Velasquez.txt'):
        return super().parsing(file)


class ConorMcGregor(Sport):
    def __init__(self):
        super().__init__('https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D0%BA%D0%B3%D1%80%D0%B5%D0%B3%D0%BE%D1%80,_%D0%9A%D0%BE%D0%BD%D0%BE%D1%80')

    def start(self):
        super().start()
        element = self.elements[2].get_attribute('innerHTML')
        with open('Conor McGregor.txt', 'w') as output:
            output.write(element)

    def parsing(self, file='Conor McGregor.txt'):
        html = super().parsing(file)
        html
        return 0


conor = ConorMcGregor()
print(conor.parsing())

# Fonbet
# c = Myclass()
# # c.start()
# result = pd.DataFrame(BeautifulSoup(c.parsing(), 'html.parser').select('div'))
# result.to_excel('output.xlsx')
# # В список
# info = []
# for row in range(len(result)):
#     info.append(str(result.ix[row, 0]))
#
# print(len(info))
#
# # Только те которые содержат
# info = [inf for inf in info if 'top-event-item__market--2MVc- _style_row-' in inf]
# for i in range(len(info)):
#     for j in range(i + 1, len(info)):
#         if info[i] in info[j]:
#             info[i] = ''
# print(len(info))
# pd.DataFrame(np.transpose([info])).to_excel('output.xlsx')
