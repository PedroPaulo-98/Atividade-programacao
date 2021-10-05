import Bancos

id = input('Id: ')
celular = input('Celular: ')
telefone = input('Telefone: ')
email = input('Email: ')

con = Bancos.conexao()
cur = con.cursor()

sql = 'UPDATE contatos SET celular = ?, telefone = ?, email = ? WHERE id = ?'

cur.execute(sql, (celular, telefone, email, id))

con.commit()
con.close()

print(f'Id {id} atualizado com sucesso.')