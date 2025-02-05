from busca_bing import busca_bing
from busca_google import busca_google
import os
from junta_arquivos import list_join

while True:

    print('Busca Bot')
    print('Em qual ferramenta deseja fazer a busca?')
    print('1 - Google | 2 - Bing(Em Construção)')
    opcao = input('-> ')
    os.system('cls')

    if opcao == '1':
        busca_google()
    
    if opcao == '2':
        busca_bing()

    os.system('cls')
    
    print('O que deseja fazer?')
    print('1 - Outra busca | 2 - Sair | 3 - Juntar Arquivos')
    escolha = input('-> ')
    os.system('cls')


    
    
    if escolha == '2':
        break
    
        exit()

    if escolha == '3':
        list_join()
