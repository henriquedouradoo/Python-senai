import mysql.connector

meubanco = mysql.connector.connect(
    host = 'localhost',
    user = 'root', 
    password = 'Senai125@',
    database = 'bigdata'
)

print(meubanco)

meucursor = meubanco.cursor()

sql = 'INSERT INTO frutas (nome, quantidade, pais) VALUES (%s, %s, %s)'
valores = [
    ('Maça', 25, 'Brasil'),
    ('Banana', 40, 'México'),
    ('Morango', 30, 'Itália'),
    ('Manga', 12, 'Rússia'),
    ('Pera', 22, 'Grécia'),
    ('Amora', 56, 'Bolivia'),
    ('Uva', 45, 'França'),
    ('Laranja', 93, 'EUA')
]

try:
    sql = 'INSERT INTO frutas (nome, quantidade, pais) VALUES (%s, %s, %s)'
    meucursor.executemany(sql, valores)
    meubanco.commit()
    print(meucursor.rowcount, 'Registros Inseridos!!')
except Exception as e:
    print(f'Encontrados alguns erros ao inserir os Registros: {e}')


meucursor.execute('SELECT * FROM frutas')
registros = meucursor.fetchall()

for registro in registros:
    print(registro)


meucursor.close()
meubanco.close()