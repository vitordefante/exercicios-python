from time import sleep


def remover(lst):
    import pickle

    while True:
        try:
            deletar = int(input('\033[1;34mNúmero do usuário que deseja remover (-1 sai): \033[m'))
            if deletar == -1:
                break
            del lst[deletar]
            pickle.dump(lst, open("pessoas.dat", "wb"))
            print('\033[1;33mCadastro removido.\033[m')
            sleep(0.30)
            return

        except(ValueError, TypeError, IndexError):
            print('\033[11;31mCódigo inválido, tente novamente.\033[m')
            continue


def cadastros(lst):
    lst.sort()
    print('\n\033[1;33m               Pessoas cadastradas\n\033[m')

    for c in range(0, len(lst)):
        print('{}  {:<40} {} anos'.format(c, lst[c][0], lst[c][1]))


def cadastrar(lst):
    import pickle
    pessoa = (str(input('Nome: ').strip().title()), int(input('Idade: ')))
    lst.append(pessoa)
    print('Cadastro efetuado.')
    pickle.dump(lst, open("pessoas.dat", "wb"))


def menu(lst):
    while True:

        print('\n\033[1;33mMenu principal\033[m')
        print('\033[1;33m1.\033[1;34m Ver pessoas cadastradas\n'
              '\033[1;33m2.\033[1;34m Cadastrar nova Pessoa\n'
              '\033[1;33m3.\033[1;34m Remover cadastro\n'
              '\033[1;33m4.\033[1;34m Sair do Sistema')

        while True:
            try:
                opcao = int(input())
                break
            except(ValueError, TypeError):
                print('\033[1;31mOpçao inválida, tente novamente.\033[m')

        if opcao == 1:
            cadastros(lst)
        elif opcao == 2:
            cadastrar(lst)
        elif opcao == 3:
            remover(lst)
        elif opcao == 4:
            print('\033[1;33mEncerrando o programa...\033[m')
            sleep(0.30)
            break
