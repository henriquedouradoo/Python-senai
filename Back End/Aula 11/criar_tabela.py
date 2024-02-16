import mysql.connector

meubanco = mysql.connector.connect(
    host = 'localhost',
    user = 'root', 
    password = 'Senai125@',
    database = 'bigdata'
)

print(meubanco)

meucursor = meubanco.cursor()
sql = 'CREATE TABLE frutas (nome VARCHAR(50) NOT NULL, quantidade INT DEFAULT 0, pais VARCHAR(30), PRIMARY KEY(NOME))'
meucursor.execute(sql)
print('Tabela Criada.')

meubanco.commit()