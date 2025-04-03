from funcoes import *
def listaClientes(situacao):
    vsql="SELECT * FROM clientes " 
    if situacao!='':
        vsql+=" WHERE ativo="+str(situacao)
    vconexao=conexao.ConexaoBanco()
    resultado=conexao.consulta(vconexao,vsql)
    vconexao.close()
    return resultado    

def SaldoCliente(idCliente):
    vsql="SELECT cc.id, tc.descricao, c.nome, cc.saldo   FROM contasClientes as cc JOIN clientes as c on c.id = cc.id_cliente JOIN tiposContas as tc on tc.id=cc.id_tipoConta WHERE cc.id_cliente="+str(idCliente)
    vconexao=conexao.ConexaoBanco()
    resultado=conexao.consulta(vconexao,vsql)
    vconexao.close()
    return resultado    
