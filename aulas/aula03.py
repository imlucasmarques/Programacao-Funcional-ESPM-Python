import mysql.connector

con = mysql.connector.connect(host='localhost', database='sakila', user='root', password='root')
print("Conectado!")

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(50), tel VARCHAR(40)
    )
"""

tabela_emails = """
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY, dono VARCHAR(50)
    )
"""

cursor = con.cursor()
cursor.execute(tabela_contatos)
cursor.execute(tabela_emails)

cursor.execute('INSERT INTO contatos(nome, tel) VALUES (%s, %s)', ('João', '11212'))
cursor.execute('INSERT INTO contatos(nome, tel) VALUES (%s, %s)', ('Maria', '131331'))
cursor.execute('INSERT INTO contatos(nome, tel) VALUES (%s, %s)', ('José', '114141'))

con.commit()

sql = 'SELECT tel, nome FROM CONTATOS'

cursor.execute(sql)

for contato in cursor.fetchall():
    print(contato)


con.close()
