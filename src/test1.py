'''
Created on Jun 20, 2020

@author: MICHELLESchmidt

'''
""""import sqlite3
db=sqlite3.connect('conectaComunidade.db') """


import sqlite3

conn = sqlite3.connect('teste.db')
sqlite3.version
print (sqlite3.version);

cursor = conn.cursor()

# lendo os dados
cursor.execute("SELECT * FROM teste1;")

for linha in cursor.fetchall():
    print(linha)

conn.close()
