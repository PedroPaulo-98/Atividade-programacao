import Banco
m=1
while m:
    print ("Minhas musicas")
    print("1. Listar. \n" "2. Cadastrar. \n" "3. Alterar. \n" "4. Excluir. \n")
    m = int(input("Opção: "))
    if(m==1):
        con = Banco.conexao()
        cur = con.cursor()

        sql = 'SELECT * FROM musicas'

        cur.execute(sql)

        musicas = cur.fetchall()

        print(f'\nMúsicas [Total:{len(musicas)}]')

        for musica in musicas:
            print(f'\nID: {musica[0]}')
            print(f'NOME: {musica[1]}')
            print(f'ARTISTA: {musica[2]}')
            print(f'ÁLBUM: {musica[3]}')
            print(f'ANO: {musica[4]}')
            print(f'ARQUIVO: {musica[5]}')

        con.close()
        print("\n ---------------------------------- \n")
    if(m==2):
        nome = input('Nome: ')
        artista = input('Artista: ')
        album = input('Álbum: ')
        ano = int(input('Ano: '))
        arquivo = input('Arquivo: ')

        con = Banco.conexao()
        cur = con.cursor()

        sql = 'INSERT INTO musicas(nome, artista, album, ano, arquivo) VALUES (?, ?, ?, ?, ?)'

        cur.execute(sql, (nome, artista, album, ano, arquivo))

        con.commit()
        con.close()

        print('Música cadastrada com sucesso.')
        print("\n ---------------------------------- \n")
    if(m==3):
        id = input('Id: ')
        nome = input('Nome: ')
        artista = input('Artista: ')
        album = input('Álbum: ')
        ano = int(input('Ano: '))
        arquivo = input('Arquivo: ')

        con = Banco.conexao()
        cur = con.cursor()

        sql = 'UPDATE musicas SET nome = ?, artista = ?, album = ?, ano = ?, arquivo = ? WHERE id = ?'

        cur.execute(sql, (nome, artista, album, ano, arquivo, id))

        con.commit()
        con.close()

        print(f'Id {id} atualizado com sucesso.')
        print("\n ---------------------------------- \n")
    if(m==4):
        id = input('Id: ')

        con = Banco.conexao()
        cur = con.cursor()

        sql = 'DELETE FROM musicas WHERE id = ?'

        cur.execute(sql, (id,))

        con.commit()
        con.close()

        print(f'Id {id} excluído com sucesso.')
        print("\n ---------------------------------- \n")

