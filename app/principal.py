from funcoes import *

print('PROGRAMA DE OPERAÇÕES BANCARIAS...')

operacao = 1
while operacao != 0:
    print('----------------------------------------')
    operacao=menuPrincipal()
    print(operacao)
    print('----------------------------------------')
    match operacao:
        case 1:
            os.system('cls')
            print('MENU TABELAS')
            print( menuTabelas())
        case 2:
            os.system('cls')
            print('MENU CLIENTES')
            file=path() + '/clientes.py'
            subprocess.run(['python', file])
        case 3:
            os.system('cls')
            print('MENU AGÊNCIAS')
            file=path() + '/agencias.py'
            subprocess.run(['python', file])
        case 4:
            os.system('cls')
            print('MENU OPERAÇÕES BANCARIAS')
            file=path() + '/contasClientes.py'
            subprocess.run(['python', file])
        case 5:
            os.system('cls')
            print('MENU RELATÓRIOS')
            file=path() + '/relatorios.py'
            subprocess.run(['python', file])
        case 0:
            operacao = 0
        case _:
            print('Opção não Reconhecida. Por favor Tente Novamente.')
print('Fim do Programa')
os.system('pause')
os.system('cls')