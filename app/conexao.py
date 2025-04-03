from funcoes import *
import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = "C:\\Cursos\\IFCE\\InternetParaWeb\\SegundoSemestre\\Banco de Dados I\\Unidade 4\\Tarefa\\miniMundo\\dbf\\minimundodbf.db"
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return conexao

def Crud(conexao,sql,msg):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print(msg)
    except Error as ex:
        print(ex)

def consulta(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        resutado = c.fetchall()
        return resutado
    except Error as ex:
        print(ex)