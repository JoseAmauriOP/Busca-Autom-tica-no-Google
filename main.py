from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
pesquisa = input('O que você quer buscar?')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.google.com')
time.sleep(5)
busca = driver.find_element(By.NAME, 'q')
busca.click()
time.sleep(1)
busca.send_keys(pesquisa)
time.sleep(1)
busca.send_keys(Keys.ENTER)
time.sleep(30)
titulos = driver.find_elements(By.TAG_NAME, 'h3')
for i,titulo in enumerate(titulos):
    if titulo.text.strip():
        print(f'{i} Titulo:{titulo.text}')


time.sleep(3)
driver.quit()