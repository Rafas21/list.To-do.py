from json import load, dump
from os import system
from pathlib import Path
from tabulate import tabulate

# Limpa tela
def clean_screen():
    system('cls')

def get_data():
    return load_data(data_list, FILE_PATH)

# Metodo para parar e mostrar ao usuario algum erro
def pause():
    input('Pressione ENTER para continuar...')

# Criação e salvamento de informações no JSON
def load_data(default, FILE_PATH):
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return load(file)
    except FileNotFoundError:
        save(default, FILE_PATH)
    return default

def save(dlist, FILE_PATH):
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        dump(dlist, file, indent=2, ensure_ascii=False)
    return dlist

# Estruturas de tratamento de decisão

# Criação
def create(task,):
    data = get_data()
    data["A fazer"].append(task)
    save(data, FILE_PATH)

# Leitura
def read():
    data = get_data()

    a_fazer = data.get("A fazer",[])
    fazendo = data.get("Fazendo",[])
    feito = data.get("Feito",[])

    # Descobrir qual lista é maior para alinhar
    max_len = max(len(a_fazer), len(fazendo), len(feito))
    
    # Preencher com vazio para alinhar colunas
    a_fazer += [""] * (max_len - len(a_fazer))
    fazendo += [""] * (max_len - len(fazendo))
    feito += [""] * (max_len - len(feito))

    # Montar tabela
    tabela = list(zip(a_fazer, fazendo, feito))
    print(tabulate(tabela, headers=["A fazer", "Fazendo", "Feito"], tablefmt="grid"))
    pause()

# Atualização
def update(select, destino):
    data = get_data()
    
    if destino not in data:
        print(f'A lista "{destino}" não existe.')
    else:
        encontrado = False
        for categoria, lista in data.items():
            if select in lista:
                lista.remove(select)
                data[destino].append(select) 
                encontrado = True
                print(f'Tarefa "{select}" movida de "{categoria}" para "{destino}".')
                pause()
                break

        if not encontrado:
            print(f'A tarefa "{select}" não foi encontrada em nenhuma lista.')
            pause()
    
    save(data, FILE_PATH)

# Exclusão
def delete(remove):
    data = get_data()

    encontrado = False
    for categoria, lista in data.items():
        if remove in lista:
            lista.remove(remove)
            encontrado = True
            print(f'Tarefa "{remove}" removida.')
            pause()

    if not encontrado:
        print(f'A tarefa "{remove}" não foi encontrada em nenhuma lista.')
        pause()

    save(data, FILE_PATH)

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR.parent / "data" / "tasks.json"

data_list = load_data({"A fazer":[], "Fazendo":[], "Feito":[]}, FILE_PATH)