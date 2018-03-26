import sqlite3

caminho = "/tmp/"
banco = r"arprotect.db"

def criar_tabelas(): 
    conexao = sqlite3.connect(caminho+banco)   
    c = conexao.cursor()
    c.execute("""create table if not exists produto (codigo integer primary key autoincrement,
    descricao text,fornecedor integer, garantia int, data_entrada date text,
    tipo_escritorio integer,tipo_vigilancia integer, 
    tipo_informatica integer tipo_infra integer, 
    tipo_outros integer, observacao text);""")
    
    c.execute("""create table if not exists fornecedor (codigo integer primary key autoincrement,
    descricao text, nome text, endereco text, telefone text, site text,
    classificacao_otimo integer, classificacao_bom integer,classificacao_regular integer,
    classificacao_ruim integer, observacoes text);""")

    c.execute("""create table if not exists usuario (codigo integer primary key autoincrement, nome text , senha text);""")
    conexao.close()

def inserir_usuario(usuario,senha):
    conexao = sqlite3.connect(caminho+banco)
    c = conexao.cursor()
    lista = [usuario,senha]
    c.execute("insert into usuario (nome, senha) values (?,?);",lista)
    conexao.commit()
    conexao.close()

def inserir_fornecedor2(codigo,descricao,nome,endereco,telefone,site,classificacao_otimo,classificacao_bom,
    classificacao_regular,classificacao_ruim,observacoes):    
    conexao = sqlite3.connect(caminho+banco)
    c = conexao.cursor()
    lista = [codigo,descricao,nome,endereco,telefone,site,classificacao_otimo,classificacao_bom,
    classificacao_regular,classificacao_ruim,observacoes]
    c.execute("insert into fornecedor values (?,?,?,?,?,?,?,?,?,?,?)",lista)
    conexao.commit()
    conexao.close()

def inserir_fornecedor(codigo,descricao,nome,endereco,telefone,site):    
    conexao = sqlite3.connect(caminho+banco)
    c = conexao.cursor()
    lista = [codigo,descricao,nome,endereco,telefone,site]
    c.execute("insert into fornecedor (codigo,descricao,nome,endereco,telefone,site) values (?,?,?,?,?,?)",lista)
    conexao.commit()
    conexao.close()

def pegar_usuario():
    conexao = sqlite3.connect(caminho+banco)
    c = conexao.execute("select * from usuario")
    return c.fetchall()

def pegar_fornecedor():
    conexao = sqlite3.connect(caminho+banco)
    c = conexao.cursor()
    return c.execute("select * from fornecedor")

criar_tabelas()
inserir_usuario("greg","123")