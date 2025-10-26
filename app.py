import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '*Leticia06*',
    database =  'alianca_corp'
)

cursor = conexao.cursor()

##__________________________________________________________________________

print('[1] Inserir dados \n[2] Atualizar dados \n[3] Excluir dados' )

pergunta = int(input('O que você deseja fazer? '))

##__________________________________________________________________________

##INSERÇÃO DO DEPARTAMENTO
if pergunta == 1:
    
    insert_dp = input('Qual departamento você deseja inserir? ')
    comando = 'INSERT INTO departamento (nome_departamento) VALUES (%s)'
    cursor.execute (comando, (insert_dp, ))
    conexao.commit()

    cursor.execute('SELECT * FROM departamento;')
    resultado = cursor.fetchall()
    print(resultado)

    cursor.close()
    conexao.close()

##__________________________________________________________________________

##ATUALIZAÇÃO DO DEPARTAMENTO
elif pergunta == 2:

    cursor.execute('SELECT * FROM departamento;')
    resultado = cursor.fetchall()
    print(resultado)

    id_dp = input('Digite o id do departamento que você deseja alterar: ')
    novo_dp = input('Qual é o novo nome do departamento escolhido? ')
    
    comando = '''UPDATE departamento
    SET nome_departamento = %s
    WHERE departamento_id = %s'''

    cursor.execute(comando, (novo_dp, id_dp))
    conexao.commit()

    cursor.execute('SELECT * FROM departamento')
    resultado = cursor.fetchall()
    print(resultado)

    cursor.close()
    conexao.close()

##__________________________________________________________________________

##EXCLUSÃO DO DEPARTAMENTO
elif pergunta == 3:

    cursor.execute('SELECT * FROM departamento;')
    resultado = cursor.fetchall()
    print(resultado)

    excl_dp = input('Qual é o id do departamento que deseja excluir? ')
    comando = '''DELETE FROM departamento
    WHERE departamento_id = %s'''
    cursor.execute(comando, (excl_dp, ))
    conexao.commit()

    cursor.execute('SELECT * FROM departamento')
    resultado = cursor.fetchall()
    print(resultado)

    cursor.close()
    conexao.close()

##__________________________________________________________________________








