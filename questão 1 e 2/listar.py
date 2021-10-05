import Bancos
con = Bancos.conexao()
cur = con.cursor()

sql = 'SELECT * FROM contatos'

cur.execute(sql)

listar = cur.fetchall()

print(f'\nContatos [Total:{len(listar)}]')

for contatos in listar:
    print(f'\nID: {contatos[0]}')
    print(f'NOME: {contatos[1]}')
    print(f'CELULAR: {contatos[2]}')
    print(f'TELEFONE: {contatos[3]}')
    print(f'EMAIL: {contatos[4]}')
    print(f'ANIVERSÁRIO: {contatos[5]}')

con.close()
