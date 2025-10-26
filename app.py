import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '*Leticia06*',
    database =  'alianca_corp'
)

cursor = conexao.cursor()


dep = input(str('Qual departamento você deseja inserir? '))
cursor.execute('INSERT INTO departamento (nome_departamento) VALUES (%s);', (dep, ))
conexao.commit()


cursor.execute('SELECT * FROM departamento;')
resultado = cursor.fetchall()
print(resultado)


nome = input('Qual é o novo nome do departamento escolhido? ')
id = input('Digite o id do departamento que você deseja alterar: ')


cursor.execute('''UPDATE departamento
SET nome_departamento = %s
WHERE departamento_id = %s;''',(nome, id))

conexao.commit()

cursor.execute('SELECT * FROM departamento')
resultado2 = cursor.fetchall()
print(resultado2)



excl = input('Qual é o id do departamento que deseja excluir? ')
cursor.execute('''DELETE FROM departamento
WHERE departamento_id = %s;''', (excl, ))
conexao.commit()

cursor.execute('SELECT * FROM departamento')
resultado3 = cursor.fetchall()
print(resultado3)






cursor.close()
conexao.close()