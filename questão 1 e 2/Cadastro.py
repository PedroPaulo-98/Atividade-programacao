import Bancos
nome = input('Nome: ')
celular = input('Celular: ')
telefone = input('Telefone: ')
email = input('Email: ')
aniversario = input('Aniversário: ')

con = Bancos.conexao()
cur = con.cursor()

sql = 'INSERT INTO contatos(nome, celular, telefone, email, aniversario) VALUES (?, ?, ?, ?, ?)'

cur.execute(sql, (nome, celular, telefone, email, aniversario))

con.commit()
con.close()

print(f'{nome} cadastrado com sucesso.')