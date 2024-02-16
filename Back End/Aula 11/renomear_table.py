import mysql.connector

meubanco = mysql.connector.connect(
    host = 'localhost',
    user = 'root', 
    password = 'Senai125@',
    database = 'bigdata'
)

print(meubanco)

meucursor = meubanco.cursor()

try:
    meucursor.execute('ALTER TABLE isaac_paixao RENAME TO frutas_variadas')
    print('Tabela Renomeada com Sucesso. ')
except:
    print('Ocorreu algum erro ao renomear a tabela')