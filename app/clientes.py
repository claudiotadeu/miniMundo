from funcoes import *
from ClientesController import *

operacao = 1
while operacao != 0:
    operacao = menuClientes()
    match operacao:
        case 1:
            print('NOVO CLIENTE')
            nome = input("Digite o Nome do Cliente: ")
            cidade = input("Digite a Cidade do Cliente: ")
            ativo = input("Situação: Digite [1] Para Inativo ou [0] Para Ativo: ")
            ativo = validaSituacao(ativo)
            while ativo != 0 and ativo != 1:
                print('Opção de Situação Inexistente!!!')
                ativo = input("Digite [0] Para Inativo ou [1] Para Ativo: ")
                ativo = validaSituacao(ativo)
            ClienteController.InserirCliente(nome,cidade,int(ativo))

        case 2:
            print('ALTERAR CLIENTES')
            registro = input('Digite o nome do Cliente: ')
            resultado = ClienteController.PesquisaCliente('nome',registro)
            if resultado:
                idRegistro = resultado
            else:
                idRegistro = input('Digite o ID do Registro a ser Alterado: ')

            confirmacao = input("O REGISTRO SERÁ ALTERADO PERMANETEMENTE.\nCONTINUAR COM A OPERAÇÃO? [S][N] ")
            if confirmacao == "S":
                dado = int(input("Que dado deseja alterar:\n[1] Nome\n[2] Endereço\n[3] Situação\n[0] Para Cancelar\n"))
                if dado > 0 and dado < 4:
                    match dado:
                        case 1:
                            chave = "nome"
                        case 2:
                            chave = "endereco"
                        case 3:
                            chave = "ativo"
                        case _:
                            print("Opção Inválida!!!")

                novoDado = input("Digite o Novo Dado: ")
                ClienteController.AtualizarCliente(chave,novoDado,idRegistro)
            else:
                print("Operação Cancelada!")

        case 3:
            print('EXCLUIR CLIENTE')
            registro = input('Digite Nome do Cliente: ')
            resultado = ClienteController.PesquisaCliente('nome',registro)
            if resultado:
                registro = resultado
            else:
                registro = input('Digite o ID do Registro a ser Excluido: ')

            confirmacao=input("O REGISTRO SERÁ EXCLUIDO PERMANETEMENTE.\nCONTINUAR COM A OPERAÇÃO? [S][N] ")
            if confirmacao == "S":
                ClienteController.ExluiCliente(registro)
            else:
                print("Operação Cancelada!")

        case 4:
            print('LISTAR CLIENTES')
            lista = ClienteController.listar()
            os.system('cls')
            print("Total de Registros Cadastrados: " + str(len(lista)))
            limiteLinhas=3
            contador = 0
            for l in lista:
                posicao = (l[3])
                if posicao == 1:
                    posicao='Ativo'
                else:
                    posicao='Inativo'
                print("ID: {0: <3} Nome: {1: <30} Endereço: {2: <25} Situação: {3: <10}".format(str(l[0]),l[1],str(l[2]),posicao ))
                contador += 1
                if(contador >= limiteLinhas):
                    contador = 0
                    os.system('pause')
                    os.system('cls')
            print('Fim da Lista')
            os.system('pause')
            
        case 0:
            print('Sair')
            operacao = 0

        case _:
            print('Opção não Reconhecida. Por favor Tente Novamente.')