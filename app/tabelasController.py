from funcoes import *

def listaTipoConta():
    sql = "SELECT * FROM tiposContas WHERE ativo=1"
    conexao = conexao.ConexaoBanco()
    resultado = conexao.consulta(conexao,sql)
    conexao.close()
    return resultado    

def listaNaturezaMovimentacao():
    sql = "SELECT * FROM naturezasMovimentacao WHERE ativo=1"
    conexao = conexao.ConexaoBanco()
    resultado = conexao.consulta(conexao,sql)
    conexao.close()
    return resultado    
