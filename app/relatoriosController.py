from funcoes import *
def listaClientes(situacao):
    sql = "SELECT * FROM clientes " 
    if situacao!='':
        sql +=" WHERE ativo="+str(situacao)
    conexao = conexao.ConexaoBanco()
    resultado = conexao.consulta(conexao,sql)
    conexao.close()
    return resultado    

def SaldoCliente(idCliente):
    sql = "SELECT cc.id, tc.descricao, c.nome, cc.saldo   FROM contasClientes as cc JOIN clientes as c on c.id = cc.id_cliente JOIN tiposContas as tc on tc.id=cc.id_tipoConta WHERE cc.id_cliente="+str(idCliente)
    conexao = conexao.ConexaoBanco()
    resultado = conexao.consulta(conexao,sql)
    conexao.close()
    return resultado    
