import mysql.connector

banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root', 
    password = 'Senai125@',
    database = 'bigdata'
)

meucursor = banco.cursor()

# Realizar uma consulta, deleção, atualização ou inserção no Banco de Dados
meucursor.execute('SELECT * FROM frutas')

# Armazenar o resultado do select em uma variável
resultados = meucursor.fetchall()

# Maneira 1 de exibir os dados da Consulta
print(resultados)

# Maneira 2 (mais organizada)
for registros in resultados:
    print(registros)

# DELETAR REGISTROS NA TABELA

# Deletar um Registro com Critério
try:
    meucursor.execute("DELETE FROM frutas WHERE nome = 'Amora'")
    print('Registros excluídos com Sucesso!')  

except:
    print('Não foi possível excluir. Verificar o nome/valor digitado ou o comando')
   
# Selecionar uma o mais colunas para serem exibidas
meucursor.execute('SELECT nome, pais FROM frutas')
resultados2 = meucursor.fetchall()
for registros2 in resultados2:
    print(registros2[0], "-", registros2[1])


# Atualizar uma coluna com valor IGUAL

try:
    meucursor.execute("UPDATE frutas SET pais='Brasil'")
    print('Atualização do País concluída com Êxito')
except:
    print('Não foi possível realizar a atualização')    
meucursor.execute('SELECT nome, pais FROM frutas')

resultados3 = meucursor.fetchall()
for registros3 in resultados3:
    print(registros3[0], "-", registros3[1])


# Quando executarmos ATUALIZAÇÃO, EXCLUSÃO OU INCLIÇÃO, devemos usar o COMMIT
banco.commit()
