from funcoes import *
from tabelasController import *
from ClientesController import *
from ContasClientesController import *
from AgenciaController import *

operacao = 1
situacaoAtivo = 1
while operacao !=  0:
    operacao = menuOperacoesBancarias()
    match operacao:
        case 1:
            print('NOVA CONTA')
            cidadeAgencia = input('Digite a Cidade da Agência: ')
            resultado = AgenciaController.PesquisaAgencia('cidade',cidadeAgencia)
            if resultado:
                idAgencia = resultado[0]
            else:
                idAgencia = input('Digite o ID do Registro a ser Alterado: ')
            
            listaTiposDeContas =  listaTipoConta()
            for l in listaTiposDeContas:
                posicao  =  (l[3])
                if posicao  ==  1:
                    posicao = 'Ativo'
                else:
                    posicao = 'Inativo'
                print("ID: {0: <3} Tipo da Conta: {1: <30} Taxa de Juros: {2: <25} Situação: {3: <10}".format(str(l[0]),l[1],str(l[2]),posicao ))
            idTipoConta = input('Digite o ID do Registro a ser Alterado: ')
           
            nomeCliente = input('Digite o Nome do Cliente: ')
            resultado = ClienteController.PesquisaCliente('nome',nomeCliente)
            if resultado:
                idCliente = resultado
            else:
                idCliente = input('Digite o ID do Cliente: ')

            data_abertura = datetime.today().strftime("%d/%m/%Y")
            print(idAgencia,idTipoConta,idCliente, 0, '02/04/2025', 1)
            ContaClienteController.InserirContaCliente(idAgencia,idTipoConta,idCliente, str(0), str(data_abertura), str(1))

        case 2:
            print('EFETUAR DEPOSITO')
            nomeCliente = input('Digite o Nome do Cliente: ')
            listaContas = ContaClienteController.ConsultaExiteConta(nomeCliente)
            print('Lista das Contas Existentes')
            for l in listaContas:
                print("Número da Conta: {0: <3} Nome do Cliente: {1: <30} Tipo da Conta: {2: <25}".format(str(l[0]),l[1],l[2]))

            validaConta = False
            contador = 0
            while validaConta  == False:
                idcontaCliente = int(input('Digite o Número da Conta: '))
                for l in listaContas:
                    contador += 1
                    if idcontaCliente == l[0]:
                        situacaAtualConta = int(l[0][5])
                        if situacaoAtivo == situacaAtualConta:
                            validaConta = True
                        else:
                            print('ATENÇÃO, CONTA INATIVA')
                    
                    if contador >= len(listaContas) and validaConta == False:
                        print('Conta Inexistente, Por Favor Digitar Um Número de Válida: ')

            print('Número da Conta válida!!! Prosseguir....')
            os.system('pause')
            os.system('cls')
            natureza = 1
            valor = float(input('Digite o Valor do Depósito no Formato 0.00: '))
            ContaClienteController.Deposito(idcontaCliente,natureza,valor)

        case 3:
            print('EFETUAR SAQUE')
            nomeCliente = input('Digite o Nome do Cliente: ')
            listaContas = ContaClienteController.ConsultaExiteConta(nomeCliente)
            print('Lista das Contas Existentes')
            for l in listaContas:
                print("Número da Conta: {0: <3} Nome do Cliente: {1: <30} Tipo da Conta: {2: <25}".format(str(l[0]),l[1],l[2]))

            validaConta = False
            contador = 0
            while validaConta == False:
                idcontaCliente =  int(input('Digite o Número da Conta: '))
                for l in listaContas:
                    contador +=  1
                    if idcontaCliente == l[0]:
                        situacaAtualConta =  int(l[0][5])
                        if situacaoAtivo == situacaAtualConta:
                            validaConta =  True
                        else:
                            print('ATENÇÃO, CONTA INATIVA')
                    
                    if contador >= len(listaContas) and validaConta == False:
                        print('Conta Inexistente, Por Favor Digitar Um Número de Válida: ')
            print('Número da Conta válida!!! Prosseguir....')
            os.system('pause')
            os.system('cls')
            natureza = 1
            valor =  float(input('Digite o Valor do Depósito no Formato 0.00: '))
            ContaClienteController.Saque(idcontaCliente,natureza,valor)

        case 4:
            print('APLICAR TAXA DE JUROS')
            nomeCliente =  input('Digite o Nome do Cliente: ')
            listaContas =  ContaClienteController.ConsultaExiteConta(nomeCliente)
            print('Lista das Contas Existentes')
            for l in listaContas:
                print("Número da Conta: {0: <3} Nome do Cliente: {1: <30} Tipo da Conta: {2: <25}".format(str(l[0]),l[1],l[2]))

            validaConta =  False
            contador =  0
            while validaConta == False:
                idcontaCliente =  int(input('Digite o Número da Conta: '))
                for l in listaContas:
                    contador += 1
                    if idcontaCliente == l[0]:
                        situacaAtualConta =  int(l[0][5])
                        if situacaoAtivo == situacaAtualConta:
                            taxaJuros =  l[3]
                            validaConta =  True
                        else:
                            print('ATENÇÃO, CONTA INATIVA')
                    
                    if contador >= len(listaContas) and validaConta==False:
                        print('Conta Inexistente, Por Favor Digitar Um Número de Válida: ')
            print('Número da Conta válida!!! Prosseguir....')
            os.system('pause')
            os.system('cls')
            natureza = 1
            taxaJuros =  float(taxaJuros)
            ContaClienteController.AplicarTaxaJurosPoupanca(idcontaCliente,natureza,taxaJuros)
          
        case 5:
            print('ENCERRAR CONTA')
            nomeCliente =  input('Digite o Nome do Cliente: ')
            listaContas =  ContaClienteController.ConsultaExiteConta(nomeCliente)
            print('Lista das Contas Existentes')
            for l in listaContas:
                print("Número da Conta: {0: <3} Nome do Cliente: {1: <30} Tipo da Conta: {2: <25}".format(str(l[0]),l[1],l[2]))

            validaConta =  False
            contador =  0
            while validaConta == False:
                idcontaCliente=int(input('Digite o Número da Conta: '))
                for l in listaContas:
                    contador += 1
                    if idcontaCliente == l[0]:
                        situacaAtualConta =  int(l[0][5])
                        if situacaoAtivo == situacaAtualConta:
                            validaConta =  True
                        else:
                            print('ATENÇÃO, CONTA INATIVA')
                    
                    if contador >= len(listaContas) and validaConta==False:
                        print('Conta Inexistente, Por Favor Digitar Um Número de Válida: ')
            print('Número da Conta válida!!! Prosseguir....')
            os.system('pause')
            os.system('cls')
            confirmacao =  input("O REGISTRO SERÁ ALTERADO PERMANETEMENTE.\nCONTINUAR COM A OPERAÇÃO? [S][N] ")
            if confirmacao == "S":
                ContaClienteController.EncerrarContaCliente(idcontaCliente)
            else:
                print('OPERAÇÃO CANCELADA COM SUCESSO!')
            
        case 0:
            print('Sair')
            operacao =  0

        case _:
            print('Opção não Reconhecida. Por favor Tente Novamente.')
