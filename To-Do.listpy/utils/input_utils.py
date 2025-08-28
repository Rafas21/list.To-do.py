from services.tasks_service import create, read, update, delete, clean_screen, pause, load_data, get_data, FILE_PATH

# Validando entradas do usuario
def get_input(mensagem: str, obrigatorio: bool = True) -> str:
    data = get_data()

    while True:
        valor = (mensagem)
        for categoria, lista in data.items():
            if valor in lista:
                input("Esta tarefa ja exite, pressione ENTER para retornar...")
                return None
            else:
                if obrigatorio and not valor:
                    print("Esse campo é obrigatório. Tente novamente.")
                    pause()
                    return None
                else:
                    return valor

# Validando casos
def fsystem(position):
    match position:

        case 1:
            task = input('Digite a tarefa: ').capitalize().strip()
            verified = get_input(task)
            if verified is not None:
                create(verified)
            clean_screen()
            
        case 2:
            read()
            clean_screen()

        case 3:
            select = input('Qual tarefa gostaria de mudar ? ').capitalize().strip()
            destino = input('Para qual lista gostaria de mover ? ').capitalize().strip()
            listas_validas = ["A fazer", "Fazendo", "Feito"]
            if destino not in listas_validas:
                print("Lista inválida. Escolha entre:", ", ".join(listas_validas))
                return  
            update(select, destino)
            clean_screen()

        case 4:
            remove = input('Qual tarefa gostaria de remover ? ').capitalize().strip()
            delete(remove)
            clean_screen()
            