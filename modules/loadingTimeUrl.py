import sys
import timeit
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import csv
from datetime import datetime
from modules.failureControl import *

fc = FailureControl()

config = open('C:/Automations/loadingTimeUrl/input/url.txt', 'r').readlines()
list_config = []

class LoadingTimeUrl():
    def __init__(self):
        pass

    def timeUrl(self):
        try:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("dom.popup_maximum", 0)
            browser = webdriver.Firefox(executable_path='C:/Automations/loadingTimeUrl/path/geckodriver',firefox_profile=profile)
        except:
            #browser = webdriver.Chrome('C:/Automations/loadingTimeUrl/path/chromedriver89.exe')
            sys.exit()

        for n in config:
            timeBegin = timeit.default_timer()
            system = (n[:n.find('=')]).strip()
            url = (n[n.find('=') + 1:]).strip()
            try:
                browser.set_page_load_timeout(30)
                browser.get(url)

                while True:
                    x = browser.execute_script("return document.readyState")
                    if x == "complete":
                        timeEnd = timeit.default_timer()
                        result = 1 if int(timeEnd - timeBegin) == 0 else int(timeEnd - timeBegin)
                        print("APP: "+ system + " demorou " +str(result) + " segundos")
                        fc.failureCleaner(system)
                        break

                self.result(system, result)

            except TimeoutException as err:
                print("Url: " + system + " **************  timeout  ****************")
                self.result(system, 30)
                fc.failureCounter(system)

            except NameError as err:
                print("Url: " + system + " **************  não carregou  ****************")
                #print(err)
                self.result(system, 30)
                fc.failureCounter(system)

            except:
                print("Url: " + system + " **************  não carregou  ****************")
                #print(err)
                self.result(system, 30)
                fc.failureCounter(system)

        browser.close()

    def result(self, system, result):
        # --------------------------- Grava Resultado no arquivo Local ---------------------------
        with open('C:/Automations/loadingTimeUrl/reports/resultLoadingTimeUrl.csv', 'a+', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([system, str(datetime.now().strftime('%d/%m/%Y')), str(datetime.now().strftime('%H:%M')), result, 'DISPONIVEL' if int(result) < 30 else 'INDISPONIVEL'])
            file.close()



