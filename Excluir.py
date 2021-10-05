import Bancos
id = input('Id: ')

con = Bancos.conexao()
cur = con.cursor()

sql = 'DELETE FROM contatos WHERE id = ?'

cur.execute(sql, (id,))

con.commit()
con.close()

print(f'Id {id} excluído com sucesso.')