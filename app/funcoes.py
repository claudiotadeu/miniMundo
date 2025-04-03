import os
from random import randrange
from datetime import datetime
import conexao
import subprocess
from ClientesController import *
from AgenciaController import *


def path():
    path=os.path.dirname(os.path.realpath(__file__))
    return path

def separadorLinha():
    print('----------------------------------------')
    print(' ')

def menuPrincipal():
    print('Tabelas  ........................[1]')
    print('Clientes  .......................[2]')
    print('Agencias ........................[3]')
    print('Operações Bancarias  ............[4]')
    print('Relatórios  .....................[5]')
    print('Sair  ...........................[0]')
    operacao=int(input('Digite uma Opção: '))
    return operacao

def menuTabelas():
    print('TIPOS DE CONTAS  ................[1]')
    print('NATUREZA DE MOVIMENTAÇÕES  ......[2]')
    print('SAIR  ...........................[0]')
    operacao=int(input('Digite uma Opção: '))
    return operacao

def menuClientes():
    print('NOVO CLIENTE  ...................[1]')
    print('ALTERAR CLIENTE  ................[2]')
    print('EXCLUIR CLIENTE  ................[3]')
    print('LISTAR CLIENTE  .................[4]')
    print('SAIR  ...........................[0]')
    operacao=int(input('Digite uma Opção: '))
    return operacao

def menuAgencias():
    print('NOVA AGÊNCIA  ...................[1]')
    print('ALTERAR AGÊNCIA  ................[2]')
    print('EXCLUIR AGÊNCIA  ................[3]')
    print('LISTAR AGÊNCIA  .................[4]')
    print('SAIR  ...........................[0]')
    operacao=int(input('Digite uma Opção: '))
    return operacao

def menuOperacoesBancarias():
    print('CRIAR CONTA  ....................[1]')
    print('DEPOSITAR .......................[2]')
    print('SACAR ...........................[3]')
    print('APLICAR TAXA DE JUROS ...........[4]')
    print('ENCERRAR CONTA ..................[5]')
    print('SAIR  ...........................[0]')
    operacao=int(input('Digite uma Opção: '))
    return operacao

def menuRelatorios():
    print('IMPRIMIR DADOS DO CLIENTE ......[1]')
    print('IMPRIMIR SALDO .................[2]')
    print('IMPRIMIR EXTRATO MOVIMENTAÇÃO ..[3]')
    print('IMPRIMIR DADOS DA CONTAS .......[4]')
    print('SAIR  ..........................[0]')
    operacao=int(input('Digite uma Opção: '))
    return operacao

def menuTiposConta():
    print('NOVO TIPO DE CONTA .............[1]')
    print('ALTERAR TIPO DE CONTA ..........[2]')
    print('EXCLUIR TIPO DE CONTA ..........[3]')
    print('LISTAR TIPOS DE CONTAS .........[4]')
    print('SAIR  ..........................[0]')
    operacao=int(input('Digite uma Opção: '))
    return operacao

def menuNaturezaMovimentacoes():
    print('NOVA NATUREZA DE MOVIMENTAÇÕES   ..[1]')
    print('ALTERAR NATUREZA DE MOVIMENTAÇÕES  [2]')
    print('EXCLUIR NATUREZA DE MOVIMENTAÇÕES  [3]')
    print('LISTAR NATUREZA DE MOVIMENTAÇÕES  .[4]')
    print('SAIR  ..........................[0]')
    operacao=int(input('Digite uma Opção: '))
    return operacao

def validaSituacao(situacao):
    situacao = situacao
    if situacao =='1':
        return 1
    elif situacao=='0':
        return 0
    else:
        return -1