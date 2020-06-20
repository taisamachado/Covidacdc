'''
Created on Jun 20, 2020

@author: MICHELLESchmidt
'''
# conectando com o banco
import sqlite3

conn = sqlite3.connect('teste2.db')
sqlite3.version
#verificando se conectou
print (sqlite3.version);
# definindo um cursor
cursor = conn.cursor();

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE teste2 (
        id INTEGER NOT NULL PRIMARY KEY ,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
);
""")
#verificando se criou
cursor = conn.execute("PRAGMA table_info(teste2);")
results = cursor.fetchall()
print(results)


# inserindo dados na tabela
cursor.execute('''
INSERT INTO teste2 (nome, idade, cpf, email)
VALUES ('Regis', 35, '00000000000', 'regis@email.com')
''')

cursor.execute('''
INSERT INTO teste2 (nome, idade, cpf, email)
VALUES ('Aloisio', 87, '11111111111', 'aloisio@email.com')
''')

cursor.execute('''
INSERT INTO teste2 (nome, idade, cpf, email)
VALUES ('Bruna', 21, '22222222222', 'bruna@email.com')
''')

# gravando no bd
conn.commit()

# puxando os dados inseridos
cursor.execute('''
SELECT * FROM teste2;
''')

for linha in cursor.fetchall():
    print(linha)

conn.close()