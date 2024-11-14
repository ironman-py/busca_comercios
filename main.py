from busca_bing import busca_bing
from busca_google import busca_google
import os

while True:

    print('Busca Bot')
    print('Em qual ferramenta deseja fazer a busca?')
    print('1 - Google | 2 - Bing')
    opcao = input('-> ')
    os.system('cls')

    if opcao == '1':
        busca_google()
    
    if opcao == '2':
        busca_bing()

    os.system('cls')
    
    print('O que deseja fazer?')
    print('1 - Outra busca | 2 - Sair')
    escolha = input('-> ')
    os.system('cls')


    
    
    if escolha == '2':
        break
    
        exit()
