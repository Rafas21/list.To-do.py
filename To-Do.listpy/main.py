from services.tasks_service import clean_screen, fsystem

#Inicio do programa
while True:
    try:
        number = int(input('\tLista de tarefas\n\n1 - Criar tarefa\n2 - Listar tarefas\n3 - Atualizar tarefa\n4 - Deletar tarefa\n\nQual opção deseja ? ' ))
    except ValueError:
        input('O programa so aceita numeros, clique ENTER para continuar...')
        clean_screen()
        continue
    
    # Estrutura de decisão
    if number < 1 or number > 4:
        input('Numero não encontrado, clique ENTER para continuar...')
        clean_screen()
    else:
        clean_screen()
        fsystem(number)
        continue
    