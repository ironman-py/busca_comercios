
import pandas as pd
import os


def list_join():

    data = {
        'nome': [],
        'telefone': []
    }


    path = os.listdir()

    for a in path:
        if os.path.isfile(a) and a.endswith('.xlsx') and a != 'lista_completa.xlsx':
            file = pd.read_excel(a)

            for nome, numero in file.values:
                data['nome'].append(nome)
                data['telefone'].append(numero)

    
    df = pd.DataFrame(data)
    with pd.ExcelWriter('lista_completa.xlsx') as writer:
        df.to_excel(writer, index=False, header=True)
    for a in path:
        if a.endswith('.xlsx') and a != 'lista_completa.xlsx':
            os.remove(a)


    
    

