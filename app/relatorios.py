from funcoes import *
from relatoriosController import *
from tabelasController import *
from ClientesController import *
from ContasClientesController import *
from AgenciaController import *

operacao = 1
situacaoEscolhida = False

while operacao != 0:
    print('----------------------------------------')
    operacao=menuRelatorios()
    print(operacao)
    print('----------------------------------------')
    match operacao:
        case 1:
            print('IMPRIMIR DADOS DO CLIENTE')
            while situacaoEscolhida == False:
                situacao=input('Escolha a Situação do Cliente - Inativo [0] / Ativos [1] ou Todos []: ')
                print(situacao)
                if situacao=="0" or situacao=="1":
                    lista=listaClientes(situacao)
                    situacaoEscolhida=True
                elif situacao=='':
                    lista=listaClientes(situacao)
                    situacaoEscolhida=True
                else:
                    print('Opção Inválida!')
                    print('Por Favor, Digite uma Opção Válida:')
                    situacao=input('Escolha a Situação do Cliente - Inativo [0] / Ativos [1] ou Todos []: ')

            for l in lista:
                situacao=l[3]
                situacao=int(situacao)
                if l[3] == 1:
                    posicao='Ativo'
                else:
                    posicao='Inativo'
                print("ID: {0: <3} Nome: {1: <30} Endereço: {2: <40} Situação: {3: <25}".format(str(l[0]),l[1],l[2],posicao ))
            situacaoEscolhida=False

        case 2:
            nomeCliente=input('Digite o Nome do Cliente: ')
            resultado=ClienteController.PesquisaCliente('nome',nomeCliente)
            if resultado:
                idCliente=resultado
            else:
                idCliente=input('Digite o ID do Cliente: ')

            lista=SaldoCliente(idCliente)
            for l in lista:
                print("ID: {0: <3} Tipo da Conta {1: <10} Nome: {2: <30} Saldo R$ : {3:.2f}".format(str(l[0]),l[1],l[2],l[3] ))

        case 3:
            print('IMPRIMIR EXTRATO MOVIMENTAÇÃO')
            """
                Extrato atual da movimentaçao da conta por cliente
            """

        case 4:
            print('IMPRIMIR DADOS DA CONTAS')
            """
                Posição Atual da Conta do Cliente
            """

        case 0:
            operacao = 0
        case _:
            print('Opção não Reconhecida. Por favor Tente Novamente.')