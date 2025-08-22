import json, os

def clean_screen():
    os.system('cls')

def load_data(dlist, FILE_PATH):
    data = []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        save(dlist, FILE_PATH)
    return data

def save(dlist, FILE_PATH):
    data = dlist
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        data = json.dump(dlist, file, indent=2, ensure_ascii=False)
    return data

def create(task):
    data = load_data()
    data.append(task)
    save(data)

def read():
    print('read')

def update():
    print('update')

def delete():
    print('delete')

FILE_PATH = "data\\tasks.json"
data_list = load_data([], FILE_PATH)

def fsystem(position):
    match position:

        case 1:
            task = input('Digite a tarefa: ')
            create(task)
            clean_screen()
            
        case 2:
            print('a')

        case 3:
            print('a')

        case 4:
            print('a')