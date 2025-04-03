from funcoes import *

class AgenciaController:
    def __init__(self, nome='', cidade='', ativo=1):
        self._nome = nome
        self._cidade = cidade
        self._ativo = ativo

    def listar():
        vsql="SELECT * FROM agencias"
        vconexao=conexao.ConexaoBanco()
        res=conexao.consulta(vconexao,vsql)
        vconexao.close()
        return res

    def InserirAgencia(nome,cidade,ativo):
        vsql="INSERT INTO agencias (nome,cidade,ativo) VALUES('"+nome+"','"+cidade+"','"+str(ativo)+"')"
        vconexao=conexao.ConexaoBanco()
        msg="Registro Inserido Com Sucesso!"
        conexao.Crud(vconexao,vsql,msg)
        vconexao.close()
        os.system("cls")

    def PesquisaAgencia(chave,registro):
        vsql="SELECT * FROM agencias WHERE "+ chave + " LIKE '%" + registro + "%'"
        vconexao=conexao.ConexaoBanco()
        resultado=conexao.consulta(vconexao,vsql)
        vconexao.close()

        for r in resultado:
            print("ID: {0: <3} Nome: {1: <30} Cidade: {2: <14} Situação: {3: <30}".format(r[0],r[1],r[2],r[3]))
        os.system("pause")
        if len(resultado) ==1:
            idAgencia=resultado[0]
            return idAgencia
        elif len(resultado) ==0:
            print('Pesquisa Sem Registros')
        else:
            print('Multiplos Registros')
            
    def ExluiAgencia(registro):
        vsql='DELETE FROM agencias WHERE id=' + str(registro)
        vconexao=conexao.ConexaoBanco()
        msg="Registro Excluido Com Sucesso!"
        conexao.Crud(vconexao,vsql,msg)
        vconexao.close()

    def AtualizarAgencia(chave,novoDado,id):
        vsql="UPDATE agencias SET " + chave + "='"+ novoDado +"' WHERE id=" + str(id)
        vconexao=conexao.ConexaoBanco()
        msg="Registro Atualizado Com Sucesso!"
        conexao.Crud(vconexao,vsql,msg)
        vconexao.close()