from funcoes import *
import conexao
import os

class ClienteController:
    def __init__(self, nome='', endereco='', ativo=1):
        self._nome = nome
        self._endereco = endereco
        self._ativo = ativo

    def listar():
        vsql="SELECT * FROM Clientes"
        vconexao=conexao.ConexaoBanco()
        resultado=conexao.consulta(vconexao,vsql)
        vconexao.close()
        return resultado

    def InserirCliente(nome,endereco,ativo):
        vsql="INSERT INTO Clientes (nome,endereco,ativo) VALUES('"+nome+"','"+endereco+"','"+str(ativo)+"')"
        vconexao=conexao.ConexaoBanco()
        msg="Registro Inserido Com Sucesso!"
        conexao.Crud(vconexao,vsql,msg)
        vconexao.close()
        os.system("cls")

    def PesquisaCliente(chave,registro):
        vsql="SELECT * FROM clientes WHERE "+ chave + " LIKE '%" + registro + "%'"
        vconexao=conexao.ConexaoBanco()
        resultado=conexao.consulta(vconexao,vsql)
        vconexao.close()

        for r in resultado:
            print("ID: {0: <3} Nome: {1: <30} endereco: {2: <14} Situação: {3: <30}".format(r[0],r[1],r[2],r[3]))
        os.system("pause")
        if len(resultado) ==1:
            idCliente=resultado[0][0]
            return idCliente
        elif len(resultado) ==0:
            print('Pesquisa Sem Registros')
        else:
            print('Multiplos Registros')
            
    def ExluiCliente(registro):
        vsql='DELETE FROM clientes WHERE id=' + str(registro)
        vconexao=conexao.ConexaoBanco()
        msg="Registro Excluido Com Sucesso!"
        conexao.Crud(vconexao,vsql,msg)
        vconexao.close()

    def AtualizarCliente(chave,novoDado,id):
        vsql="UPDATE clientes SET " + chave + "='"+ novoDado +"' WHERE id=" + str(id)
        vconexao=conexao.ConexaoBanco()
        msg="Registro Atualizado Com Sucesso!"
        conexao.Crud(vconexao,vsql,msg)
        vconexao.close()