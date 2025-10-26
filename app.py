from funções import inserir, atualizacao, exclusao, departamento

##__________________________________________________________________________

print('[1] Inserir dados \n[2] Atualizar dados \n[3] Excluir dados' )

pergunta = int(input('O que você deseja fazer? '))

##__________________________________________________________________________

##INSERÇÃO DO DEPARTAMENTO
if pergunta == 1:
    
    departamento()

    insert_dp = input('Qual departamento você deseja inserir? ')
    
    inserir(insert_dp)

##__________________________________________________________________________

##ATUALIZAÇÃO DO DEPARTAMENTO
elif pergunta == 2:

    departamento()

    id_dp = input('Digite o id do departamento que você deseja alterar: ')
    novo_dp = input('Qual é o novo nome do departamento escolhido? ')
    
    atualizacao(id_dp, novo_dp)
##__________________________________________________________________________

##EXCLUSÃO DO DEPARTAMENTO
elif pergunta == 3:

    departamento()

    excl_dp = input('Qual é o id do departamento que deseja excluir? ')
    
    exclusao(excl_dp)
##__________________________________________________________________________


