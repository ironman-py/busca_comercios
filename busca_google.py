from ddds import ddds
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
import json



def busca_google():


    bing_nome_elemento = '//span[@class="OSrXXb"]'
    tel_elemento = "//div[@class='rllt__details']/div[position()=4]"
    cidade = input('Digite o nome da cidade(sem acentos): -> ')
    categoria = input('Digite o tipo de comércio: -> ')



    contador = 1
    quantidade = {
        'nome': [],
        'telefone': []    
    }

    driver = webdriver.Chrome()
    driver.get(f'https://www.google.com/search?client=opera-gx&hs=55M&sca_esv=794ca49ae42723f1&tbm=lcl&sxsrf=AHTn8zpXBI8i6VWFgUtdLfGWr1KkOsL5lA:1738594118473&q={categoria}+em+{cidade}&rflfq=1&num=10&sa=X&ved=2ahUKEwjthtzm36eLAxXjp5UCHTcmCXAQjGp6BAgeEAE&biw=1325&bih=649&dpr=1#rlfi=hd:;si:;mv:[[-23.523536399999998,-46.6263177],[-23.5811408,-46.684060699999996]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:3')

    sleep(5)


    while contador <= 25:
        os.system('cls')
        print(f'Buscando na pagina {contador}')
        print(len(quantidade['nome']))

        itens = {
            'n': WebDriverWait(driver, 5).until(
                EC.visibility_of_all_elements_located((By.XPATH, bing_nome_elemento))
            ),

            't': WebDriverWait(driver, 5).until(
                EC.visibility_of_all_elements_located((By.XPATH, tel_elemento))
            )
        }

    
        for n, t in zip(itens['n'], itens['t']):
            number = t.text
            
                
            lista = number.split('·')
            a, b = (lista + ["Vazio", "Vazio"])[:2]
  
            numero_filtrado = ''.join(b for b in b if b not in string.punctuation).replace(' ', '')
            nome_sem_pontuacao = ''.join(n for n in n.text if n not in string.punctuation).upper()
            nome_final = unicodedata.normalize('NFD', nome_sem_pontuacao).encode('ascii', 'ignore').decode('ascii')


            for c, d in ddds():
                if cidade == c and numero_filtrado.startswith(d) and nome_final not in quantidade['nome'] and numero_filtrado not in quantidade['telefone']:
                    quantidade['nome'].append(nome_final)
                    quantidade['telefone'].append(numero_filtrado[2:])

        
        sleep(5)

        try:

            proxima = driver.find_element(By.XPATH, f'//a[@aria-label="Page {contador + 1}"]')
            proxima.click()
            contador += 1
        except Exception as e:
       
            print(f'As páginas acabaram!')
            break
    

        
        

            
        

            
     
    
                


    driver.quit()

    


    print('Listagem já disponível!')



    df = pd.DataFrame(quantidade)
    with pd.ExcelWriter(f'{cidade}_{categoria}.xlsx') as writer:
        df.to_excel(writer, index=False, header=True)

    



        
        



            

    






 

