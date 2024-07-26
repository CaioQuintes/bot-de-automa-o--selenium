import time
import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://sys.hmg.dmslog.com")
navegador.find_element('xpath',('/html/body/div/div/div/div[3]/form/div/div[1]/div[2]/input')).send_keys('CAIO.QUINTES')
time.sleep(0.5)
navegador.find_element('xpath',('/html/body/div/div/div/div[3]/form/div/div[2]/div[2]/input')).send_keys('caiogq789')
time.sleep(0.5)
pyautogui.press("enter")
#Entra no operational
navegador.find_element('xpath',('/html/body/div/div/div/nav/ul/li[5]/a')).click()
time.sleep(0.1)
#ADD
navegador.find_element('xpath',('/html/body/div/div[2]/div/div[2]/a/span')).click()
time.sleep(0.1)
#tela cheia
pyautogui.press('f11')
#documents
navegador.find_element('xpath',('/html/body/div[1]/div[2]/div/form/div[3]/div[2]/a')).click()
time.sleep(1)
#descer a pagina
#add row
navegador.find_element('xpath',('/html/body/div[1]/div[2]/div/form/div[3]/div[6]/div/div/div/div[5]/div/table/tbody/tr[2]/td/a')).click()
#navegador.find_element('xpath',('/html/body/div[1]/div[2]/div/form/div[3]/div[6]/div/div/div/div[5]/div/table/tbody/tr[2]/td/a8')).click()
time.sleep(0.5)
#numero de voo
navegador.find_element('xpath',('/html/body/div[1]/div[2]/div/form/div[3]/div[6]/div/div/div/div[5]/div/table/tbody/tr[2]/td[1]/input')).send_keys('numerodevoo')
time.sleep(0.5)
#value
navegador.find_element('xpath',('/html/body/div[1]/div[2]/div/form/div[3]/div[6]/div/div/div/div[5]/div/table/tbody/tr[2]/td[3]/input')).send_keys('value')
time.sleep(0.5)
#wigth
navegador.find_element('xpath',('/html/body/div[1]/div[2]/div/form/div[3]/div[6]/div/div/div/div[5]/div/table/tbody/tr[2]/td[4]/input')).send_keys('weigth')
time.sleep(0.5)
#insurence
navegador.find_element('xpath',('/html/body/div[1]/div[2]/div/form/div[3]/div[6]/div/div/div/div[5]/div/table/tbody/tr[2]/td[5]/input')).send_keys('insurence')

