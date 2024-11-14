from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd
from pandas import ExcelWriter
import os
import string
import unicodedata







#chrome_options = Options()

#chrome_options.add_argument("--headless")
#service = Service(ChromeDriverManager().install())

nome_elemento = "//div[@class='rllt__details']/div[position()=1]"
tel_elemento = "//div[@class='rllt__details']/div[position()=3]"

def busca_google():


    print('Digite o tipo de comércio: (Exemplo: supermercados)')
    categoria = input('Digite aqui: ')
    os.system('cls')
    print('Digite o nome da cidade: (Exemplo: São Paulo)')
    cidade = input('Digite aqui: ')
    os.system('cls')


    driver = webdriver.Chrome()



    driver.get(f'https://www.google.com/search?client=opera-gx&hs=LCt&sca_esv=976475d81eac0872&tbs=lf:1,lf_ui:10&tbm=lcl&q={categoria}+em+{cidade}&rflfq=1&num=10&sa=X&ved=2ahUKEwjA2KKE85WJAxXJHbkGHb8MApAQjGp6BAgiEAE&biw=1239&bih=601&dpr=1.5#rlfi=hd:;si:;mv:[[-2.994388,-59.932034400000006],[-3.1454831,-60.0738566]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:10')



    contador = 1
    quantidade = {
        'nome': [],
        'tel': [],
    }




    print('Buscando...')
    
    while contador <= 3:

        os.system('cls')
        print(f'Número de registros: {len(quantidade["tel"])}')

        itens = {
            'n':WebDriverWait(driver, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, nome_elemento)),
        ),
            't':WebDriverWait(driver, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH, tel_elemento))
        )
        }
          
       

        for n, t in zip(itens['n'], itens['t']):
            
         
        

        
      

            number = t.text
          
            
            lista = number.split('·')
            a, b = (lista + ["Vazio", "Vazio"])[:2]
            if b not in quantidade['tel']:
                nome_sem_pontuacao = ''.join(n for n in n.text if n not in string.punctuation).upper().replace(' ','')
                nome_final = unicodedata.normalize('NFD', nome_sem_pontuacao).encode('ascii', 'ignore').decode('ascii')
                str(quantidade['nome'].append([nome_final]))
    
                numero_filtrado = ''.join(b for b in b if b not in string.punctuation)
            
                quantidade['tel'].append(numero_filtrado)
        
     

        sleep(3)


        try:

            

            

            proxima_pagina = driver.find_element(By.XPATH, f"//a[@aria-label='Page {contador+1}']")
            proxima_pagina.click()
            contador += 1
            
            sleep(3)
        
        except Exception as e:
            print(f'As páginas acabaram!')
            break
            

        
     
    driver.quit()

   


    print('Listagem já disponível!')



    df = pd.DataFrame(quantidade)
    with pd.ExcelWriter(f'{cidade}_{categoria}.xlsx') as writer:
        df.to_excel(writer, index=False, header=True)
