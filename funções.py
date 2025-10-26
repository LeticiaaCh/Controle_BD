import mysql.connector

def conectar_bd():

    conexao = mysql.connector.connect( host = 'localhost', user = 'root', password = '*Leticia06*', database =  'alianca_corp' )

    return conexao

##__________________________________________________________________________

def departamento():

    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM departamento;')
    resultado = cursor.fetchall()
    print(resultado)

    cursor.close()
    conexao.close()
##__________________________________________________________________________

def inserir(insert_dp):

    conexao = conectar_bd()
    cursor = conexao.cursor()
    
    comando = 'INSERT INTO departamento (nome_departamento) VALUES (%s)'
    cursor.execute (comando, (insert_dp, ))

    conexao.commit()

    departamento()

    cursor.close()
    conexao.close()
##__________________________________________________________________________

def atualizacao(id_dp, novo_dp):

    conexao = conectar_bd()
    cursor = conexao.cursor()

    
    comando = '''UPDATE departamento
    SET nome_departamento = %s
    WHERE departamento_id = %s'''
    cursor.execute(comando, (novo_dp, id_dp))

    conexao.commit()

    departamento()

    cursor.close()
    conexao.close()
##__________________________________________________________________________

def exclusao(excl_dp):

    conexao = conectar_bd()
    cursor = conexao.cursor()


    comando = '''DELETE FROM departamento
    WHERE departamento_id = %s'''
    cursor.execute(comando, (excl_dp, ))

    conexao.commit()
    
    departamento()

    cursor.close()
    conexao.close()




