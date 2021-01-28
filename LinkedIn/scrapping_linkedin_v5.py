from selenium import webdriver
from time import sleep
import csv

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("https://br.linkedin.com/jobs/data-scientist-vagas")
    browser.implicitly_wait(10)
    sleep(1.5)
    visualizar_mais = browser.find_element_by_xpath("/html/body/main/div/section/button")
    vagas_totais = browser.find_elements_by_class_name('result-card__full-card-link')
    vagas_coletadas = []
    with open("descricoes_vagas.csv", 'w', encoding='latin-1') as a:
        writer = csv.writer(a, delimiter = ';', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(['ID', 'Cargo', 'Empresa', 'Local', 'Descrição'])
    
    while not len(vagas_coletadas)==len(vagas_totais):
        try:
            for x in vagas_totais[len(vagas_coletadas):]:
                browser.execute_script("return arguments[0].scrollIntoView();", x)
                sleep(.5)
                x.click()
                sleep(1)
                url_atual = browser.current_url
                id_vaga = url_atual.split('=')[1].split('&')[0]
                titulo = browser.find_element_by_class_name('topcard__title')
                empresa = browser.find_element_by_class_name('topcard__flavor')
                local = browser.find_element_by_class_name('topcard__flavor--bullet')
                descricao = browser.find_element_by_class_name('show-more-less-html__markup')
                vagas_coletadas.append(id_vaga)
                print(f"Vagas coletadas: {len(vagas_coletadas)} de {len(vagas_totais)}")
                with open("descricoes_vagas.csv", 'a', encoding='latin-1') as a:
                    writer = csv.writer(a, delimiter = ';', quoting = csv.QUOTE_MINIMAL)
                    writer.writerow([id_vaga, titulo.text, empresa.text, local.text, descricao.text])
                if visualizar_mais.is_displayed():
                    visualizar_mais.click()
                    sleep(3)
                else:
                    pass
        except:
            print("Vaga não coletada")
                
        vagas_totais = browser.find_elements_by_class_name('result-card__full-card-link')  
       
        

                       
        
    


