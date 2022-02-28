from os import system
from getpass import getpass
from time import sleep
from os import stdiomask 


def exibir_menu():
    print(
'''
[1] cadastro
[2] login
[3] sair

'''

)
    while True:
        try:
            opcao = int(input('Digite sua opção: '))
            return opcao
        except ValueError:
            print('Digite de 1 a 3')


def fazer_login():
    login = input('Nome: ')
    senha = stdiomask.getpass('Senha: ', mask='*')
    return login,senha

def buscar_usuario(login, senha):
    usuarios = []
    try:
        with open('usuarios.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                usuarios.append(linha.split())

            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[1]
                if login == nome and senha == password:
                    return True

    except FileNotFoundError:
        return False



#cadastro

while True:
        system('cls')
        opcao = exibir_menu()

        if opcao == 1:

            login, senha = fazer_login()
            if login == senha:
                print('Sua senha deve ser diferente do login')
                senha = getpass('senha: ').mask("*")
            user = buscar_usuario(login, senha)
            if user == True:
                print('Usuário ja existe!')
                sleep(2)
            else:
                with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                    arquivo.writelines(f'{login} {senha}\n')
                print('cadastro aprovado')
                exit()



        elif opcao == 2:

            login, senha = fazer_login()
            user = buscar_usuario(login,senha)
            if user == True:
                print('login realizado')
                sleep(1)
                exit()
            else:
                print('Usuário ou senha incorretos :(')
                sleep(2)


        else:
            system('cls')
            print('Até logo!')
            break