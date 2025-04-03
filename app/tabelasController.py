from funcoes import *

def listaTipoConta():
    vsql="SELECT * FROM tiposContas WHERE ativo=1"
    vconexao=conexao.ConexaoBanco()
    resultado=conexao.consulta(vconexao,vsql)
    vconexao.close()
    return resultado    

def listaNaturezaMovimentacao():
    vsql="SELECT * FROM naturezasMovimentacao WHERE ativo=1"
    vconexao=conexao.ConexaoBanco()
    resultado=conexao.consulta(vconexao,vsql)
    vconexao.close()
    return resultado    
