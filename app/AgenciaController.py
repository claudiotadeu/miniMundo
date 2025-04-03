from funcoes import *


class AgenciaController:
    def __init__(self, nome = '', cidade = '', ativo = 1):
        self._nome  =  nome
        self._cidade  =  cidade
        self._ativo  =  ativo

    def listar():
        sql = "SELECT * FROM agencias"
        conexao = conexao.ConexaoBanco()
        res = conexao.consulta(conexao,sql)
        conexao.close()
        return res

    def InserirAgencia(nome,cidade,ativo):
        sql = "INSERT INTO agencias (nome,cidade,ativo) VALUES('"+nome+"','"+cidade+"','"+str(ativo)+"')"
        conexao = conexao.ConexaoBanco()
        msg = "Registro Inserido Com Sucesso!"
        conexao.Crud(conexao,sql,msg)
        conexao.close()
        os.system("cls")

    def PesquisaAgencia(chave,registro):
        sql = "SELECT * FROM agencias WHERE "+ chave + " LIKE '%" + registro + "%'"
        conexao = conexao.ConexaoBanco()
        resultado = conexao.consulta(conexao,sql)
        conexao.close()

        for r in resultado:
            print("ID: {0: <3} Nome: {1: <30} Cidade: {2: <14} Situação: {3: <30}".format(r[0],r[1],r[2],r[3]))
        os.system("pause")
        if len(resultado)  == 1:
            idAgencia = resultado[0]
            return idAgencia
        elif len(resultado) == 0:
            print('Pesquisa Sem Registros')
        else:
            print('Multiplos Registros')
            
    def ExluiAgencia(registro):
        sql = 'DELETE FROM agencias WHERE id = ' + str(registro)
        conexao = conexao.ConexaoBanco()
        msg = "Registro Excluido Com Sucesso!"
        conexao.Crud(conexao,sql,msg)
        conexao.close()

    def AtualizarAgencia(chave,novoDado,id):
        sql = "UPDATE agencias SET " + chave + " = '"+ novoDado +"' WHERE id = " + str(id)
        conexao = conexao.ConexaoBanco()
        msg = "Registro Atualizado Com Sucesso!"
        conexao.Crud(conexao,sql,msg)
        conexao.close()