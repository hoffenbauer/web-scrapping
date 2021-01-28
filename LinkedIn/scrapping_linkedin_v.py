# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:09:12 2020

@author: Lucas
"""
from selenium import webdriver
from time import sleep
import csv
from selenium.common.exceptions import ElementClickInterceptedException

with open('vagas_ds.csv', 'w', encoding='latin-1', newline='') as vagas:
     csvwriter = csv.writer(vagas, delimiter = ';', quoting = csv.QUOTE_MINIMAL)
     csvwriter.writerow(['ID', 'Cargo', 'Local', 'Empresa'])
def scrap_linkedin():
    if __name__ == '__main__':
        browser = webdriver.Chrome()
        browser.get("https://br.linkedin.com/jobs/data-scientist-vagas")
        browser.implicitly_wait(10)
        sleep(1.5)
        visualizar_mais = browser.find_element_by_xpath("/html/body/main/div/section/button")
        
        vagas_totais = browser.find_elements_by_class_name('result-card__full-card-link')
        vagas_coletadas = []
       
        while True:
            visualizar_mais.is_displayed()
                
            try:
                for x in vagas_totais[len(vagas_coletadas):]:
                    browser.execute_script("return arguments[0].scrollIntoView();", x)
                    x.click()
                    sleep(1)
                    url_atual = browser.current_url
                    id_vaga = url_atual.split('=')[1].split('&')[0]
                    cargo = browser.find_element_by_class_name('topcard__title')
                    local = browser.find_element_by_class_name('topcard__flavor--bullet')
                    empresa = browser.find_element_by_class_name('topcard__flavor')
                    vagas_coletadas.append(id_vaga)
                    print(f'Vagas coletadas: {len(vagas_coletadas)}')
                    with open('vagas_ds.csv', 'a', encoding='utf-8', newline='') as vagas:
                        csvwriter = csv.writer(vagas, delimiter = ';', quoting = csv.QUOTE_MINIMAL)
                        csvwriter.writerow([id_vaga, cargo.text, local.text, empresa.text])
                    
                        vagas_totais = browser.find_elements_by_class_name('result-card__full-card-link')
                        
            except ElementClickInterceptedException:     
                pass
            except:
                print('Erro!')
                pass
scrap_linkedin()

