from funcoes import *

class ContaClienteController:
    def __init__(self,id_agencia=0,id_tipoConta=0, id_cliente=0, saldo=0, dataAbertura='', ativo=0):
        self._id_agencia = id_agencia
        self._id_tipoConta = id_tipoConta
        self._id_cliente = id_cliente
        self._saldo = saldo
        self._dataAbertura = dataAbertura
        self._ativo = ativo

    def ConsultaExiteConta(nomeCliente):
        sql = "SELECT cc.id as numeroConta, c.nome as nomeCliente, tc.descricao as tipoConta, tc.taxaJuros, c.ativo FROM contasClientes as cc JOIN clientes c ON c.id=cc.id_cliente JOIN tiposContas tc on tc.id=cc.id_tipoConta WHERE cc.ativo=1 " + " and c.nome LIKE '%"+nomeCliente+"%'"
        conexao = conexao.ConexaoBanco()
        resultado =   conexao.consulta( conexao, sql)
        conexao.close()
        return resultado 

    def ConsultaSaldo(id_contaCliente):
        sql =  "SELECT saldo FROM contasClientes WHERE id =  "+str(id_contaCliente)
        conexao = conexao.ConexaoBanco()
        resultado = conexao.consulta( conexao, sql)
        conexao.close()
        return resultado 

    def InserirContaCliente(id_agencia,	id_tipoConta, id_cliente, saldo, dataAbertura, ativo):
        sql = "INSERT INTO contasClientes (id_agencia,	id_tipoConta, id_cliente, saldo, dataAbertura, ativo) VALUES('"+str(id_agencia)+"','"+str(id_tipoConta)+"','"+str(id_cliente)+"','"+str(saldo)+"','"+dataAbertura+"','"+str(ativo)+"')"
        conexao = conexao.ConexaoBanco()
        msg = "Registro Inserido Com Sucesso!"
        conexao.Crud( conexao, sql,msg)
        conexao.close()
        os.system("cls")

    def Deposito(id_contaCliente,id_natureza,valor):
        sql = "INSERT INTO movimentacoesContas (id_contaCliente,id_natureza,valor) VALUES('"+str(id_contaCliente)+"','"+str(id_natureza)+"','"+str(valor)+"')"
        conexao = conexao.ConexaoBanco()
        msg = "Registro Inserido Com Sucesso!"
        conexao.Crud( conexao, sql,msg)
        conexao.close()
        resultado = ContaClienteController.ConsultaSaldo(id_contaCliente)
        saldo = resultado[0][0]
        saldo = float(saldo)
        novoSaldo =  float(valor)+saldo
        conexao =  conexao.ConexaoBanco()
        sql =  "UPDATE contasClientes SET saldo="+str(novoSaldo)+" WHERE id="+str(id_contaCliente)
        msg =  "Saldo Atualizado Com Sucesso!"
        conexao.Crud( conexao, sql,msg)
        conexao.close()
        os.system("cls")

    def Saque(id_contaCliente,id_natureza,valor):
        resultado =  ContaClienteController.ConsultaSaldo(id_contaCliente)
        saldo =  resultado[0][0]
        saldo =  float(saldo)
        if saldo >= valor:
            sql =  "INSERT INTO movimentacoesContas (id_contaCliente,id_natureza,valor) VALUES('"+str(id_contaCliente)+"','"+str(id_natureza)+"','"+str(valor)+"')"
            conexao =  conexao.ConexaoBanco()
            msg =  "Registro Inserido Com Sucesso!"
            conexao.Crud( conexao, sql,msg)
            conexao.close()
            resultado =  ContaClienteController.ConsultaSaldo(id_contaCliente)
            saldo =  resultado[0][0]
            saldo =  float(saldo)
            novoSaldo =  saldo-float(valor)
            conexao =  conexao.ConexaoBanco()
            sql =  "UPDATE contasClientes SET saldo="+str(novoSaldo)+" WHERE id="+str(id_contaCliente)
            msg =  "Saldo Atualizado Com Sucesso!"
            conexao.Crud( conexao, sql,msg)
            conexao.close()
            os.system("cls")
        else:
            print('Saldo Insuficiente!!!')

    def AplicarTaxaJurosPoupanca(id_contaCliente,id_natureza,taxaJuros):
        resultado =  ContaClienteController.ConsultaSaldo(id_contaCliente)
        saldo =  resultado[0][0]
        saldo =  float(saldo)
        calculoJuros =  (saldo*taxaJuros)/100
        sql =  "INSERT INTO movimentacoesContas (id_contaCliente,id_natureza,valor) VALUES('"+str(id_contaCliente)+"','"+str(id_natureza)+"','"+str(calculoJuros)+"')"
        conexao =  conexao.ConexaoBanco()
        msg =  "Registro Inserido Com Sucesso!"
        conexao.Crud( conexao, sql,msg)
        conexao.close()
        resultado =  ContaClienteController.ConsultaSaldo(id_contaCliente)
        saldo =  resultado[0][0]
        saldo =  float(saldo)
        novoSaldo =  float(calculoJuros)+saldo
        conexao =  conexao.ConexaoBanco()
        sql =  "UPDATE contasClientes SET saldo =  "+str(novoSaldo)+" WHERE id="+str(id_contaCliente)
        msg =  "Saldo Atualizado Com Sucesso!"
        conexao.Crud( conexao, sql,msg)
        conexao.close()
        os.system("cls")

    def EncerrarContaCliente(idcontaCliente):
        sql =  "UPDATE contasClientes SET ativo=0 WHERE id=" + str(idcontaCliente)
        conexao =  conexao.ConexaoBanco()
        msg =  "A Conta Foi Cancelada Com Sucesso!"
        conexao.Crud( conexao, sql,msg)
        conexao.close()
        os.system("cls")