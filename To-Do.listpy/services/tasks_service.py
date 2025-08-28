from json import load, dump
from os import system
from pathlib import Path
from tabulate import tabulate

# Limpa tela
def clean_screen():
    system('cls')

def c_ontinue():
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
def create(task, categoria="A fazer"):
    data = load_data(data_list, FILE_PATH)
    data[categoria].append(task)
    save(data, FILE_PATH)

# Leitura
def read(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        data = load(file)

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
    c_ontinue()

def update():
    select = input('Qual tarefa gostaria de mudar ? ')
    destino = input('Para qual lista gostaria de mover ? ')
    clean_screen()

    data = load_data(data_list, FILE_PATH)
    
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
                c_ontinue()
                break

        if not encontrado:
            print(f'A tarefa "{select}" não foi encontrada em nenhuma lista.')
            c_ontinue()
    


    save(data, FILE_PATH)

def delete():
    remove = input('Qual tarefa gostaria de remover ? ')

    data = load_data(data_list, FILE_PATH)

    encontrado = False
    for categoria, lista in data.items():
        if remove in lista:
            lista.remove(remove)
            encontrado = True
            print(f'Tarefa "{remove}" removida.')
            c_ontinue()

    if not encontrado:
        print(f'A tarefa "{remove}" não foi encontrada em nenhuma lista.')
        c_ontinue()

    save(data, FILE_PATH)

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR.parent / "data" / "tasks.json"

data_list = load_data({"A fazer":[], "Fazendo":[], "Feito":[]}, FILE_PATH)

def fsystem(position):
    match position:

        case 1:
            task = input('Digite a tarefa: ')
            create(task)
            clean_screen()
            
        case 2:
            read(FILE_PATH)
            clean_screen()

        case 3:
            update()
            clean_screen()
        case 4:
            delete()
            clean_screen()