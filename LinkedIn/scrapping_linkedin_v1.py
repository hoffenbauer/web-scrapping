#Imports
from selenium import webdriver
from time import sleep

#URL
url = "https://br.linkedin.com/jobs/search?keywords=dados&location=Brasil&geoId=106057199&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0"

#Clica apenas nos elementos de vagas
if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(url)
    sleep(1.5)
    vagas = browser.find_elements_by_class_name('result-card__full-card-link')
    
lista_descricoes_vagas = []

def coleta_vagas():
    for x in browser.find_elements_by_class_name('result-card__full-card-link'):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(.2)
        x.click()
        sleep(1)
        descricao = browser.find_element_by_class_name('description')
        lista_descricoes_vagas.append(descricao.text)  
        print(f"Vagas coletadas: {len(lista_descricoes_vagas)}")
        textos_descricoes  = "\n\n---FIM---\n\n".join(lista_descricoes_vagas)
        with open("descricoes_vagas.txt", 'w', encoding='utf-8') as a:
            a.write(textos_descricoes)
             

coleta_vagas()