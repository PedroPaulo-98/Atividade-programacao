import sqlite3

def conexao():
     return sqlite3.connect('contatodb.sqlite')



con = conexao()
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS contatos
    (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        nome        TEXT NOT NULL,
        celular     TEXT NOT NULL,
        telefone    TEXT NOT NULL,
        email       TEXT NOT NULL,
        aniversario TEXT NOT NULL
    )
''')

con.commit()
con.close()

