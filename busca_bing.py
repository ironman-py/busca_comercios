import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import os
import string
import unicodedata


def busca_bing():


    bing_nome_elemento = "//div[@class='b_vPanel']/div[position()=1]"
    bing_categoria_elemento = "//div[@class='b_vPanel']/div[position()=2]"
    bing_tel_elemento = "//div[@class='b_vPanel']/div[position()=last()]"
    bing_proxima_pagina = "//a[@class='bm_rightChevron']"
    bing_btn_reject = "//*[@id='bnp_btn_reject']/a"
    bing_campo_busca = "//textarea[@id='sb_form_q']"
    bing_btn_mais_registros = "//*[@id='lmSeeMore']/span/span[1]"

    print('Digite o tipo de comércio que deseja buscar: Ex(Supermercado)')
    tipo_comercio = input('-> ')
    os.system('cls')
    print('Digite a cidade:')
    cidade = input('-> ')
    os.system('cls')


    #Após os elementos serem encontrados, cada linha será adicionada a sua respectiva chave
    dados = {
        'nome': [],
        'telefone': [],
        'categoria': []
    }



    driver = webdriver.Chrome()
    driver.get('https://www.bing.com')

    sleep(5)

    reject_cookies = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, bing_btn_reject))
    )
    reject_cookies.click()



    paragrafo = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, bing_campo_busca))
    )

    sleep(1)
    paragrafo.click()

    sleep(3)
    paragrafo.send_keys(f"{tipo_comercio} em {cidade}" + Keys.ENTER)



    more_info = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, bing_btn_mais_registros))
    )

    sleep(3)
    more_info.click()

    sleep(5)

    contador = 1

    while contador <= 25:

        os.system('cls')
        print(f'Quantidade de páginas: {contador} | Nomes: {len(dados["nome"])} | Tel: {len(dados["telefone"])}')

        sleep(5)
        
        itens = {
            'n': driver.find_elements(By.XPATH, bing_nome_elemento),
            'c': driver.find_elements(By.XPATH, bing_categoria_elemento),
            't': driver.find_elements(By.XPATH, bing_tel_elemento)

        }
            
        
        
        for n, c, t in zip(itens['n'], itens['c'], itens['t']):
            

            nome_filtrado = ''.join(n for n in n.text if n not in string.punctuation).upper()
            nome_filtrado_sem_acentuacao = unicodedata.normalize('NFD',nome_filtrado).encode('ascii', 'ignore').decode('ascii')
            if nome_filtrado_sem_acentuacao not in dados['nome']:
                dados['nome'].append(nome_filtrado_sem_acentuacao)

                tel_filtrado = ''.join(t for t in t.text if t not in string.punctuation)
     
                dados["telefone"].append(tel_filtrado.replace(' ',''))
            
            
                dados['categoria'].append(c.text)


        try:

            proxima = driver.find_element(By.XPATH, bing_proxima_pagina)
            

            

            proxima.click()
            contador += 1

        
        


        except Exception as e:
            os.system('cls')
            print(f'Fim das páginas!')
            print('Sua listagem já está disponível')
            print(f'Registros: {len(dados["telefone"])}')

            break



    sleep(1)  

    driver.quit()





    print('Listagem já disponível!')
    df = pd.DataFrame(dados)
    with pd.ExcelWriter(f'{tipo_comercio}_{cidade}.xlsx') as writer:
        df.to_excel(writer, header=True)
        
