import Banco
m=1
while m:
    print ("Minhas Playlist")
    print("1. Listar. \n" "2. Cadastrar. \n" "3. Alterar. \n" "4. Excluir. \n" "5. Adicionar Musica. \n")
    m = int(input("Opção: "))
    if(m==1):
        con = Banco.conexao()
        cur = con.cursor()

        sql = 'SELECT * FROM playlists'

        cur.execute(sql)

        playlists = cur.fetchall()

        print(f'\nPlaylists [Total:{len(playlists)}]')

        for playlist in playlists:
            print(f'\nID: {playlist[0]}')
            print(f'NOME: {playlist[1]}')
            print(f'DATA: {playlist[2]}')

        con.close()
        print("\n ---------------------------------- \n")
    if(m==2):
        nome = input('Nome: ')
        data = input('Data: ')

        con = Banco.conexao()
        cur = con.cursor()

        sql = 'INSERT INTO playlists(nome, data) VALUES (?, ?)'

        cur.execute(sql, (nome, data))

        con.commit()
        con.close()

        print('Playlist cadastrada com sucesso.')
        print("\n ---------------------------------- \n")
    if(m==3):
        id = input('Id: ')
        nome = input('Nome: ')
        data = input('Data: ')

        con = Banco.conexao()
        cur = con.cursor()

        sql = 'UPDATE playlists SET nome = ?, data = ? WHERE id = ?'

        cur.execute(sql, (nome, data, id))

        con.commit()
        con.close()

        print(f'Id {id} atualizado com sucesso.')
        print("\n ---------------------------------- \n")
    if(m==4):
        id = input('Id: ')

        con = Banco.conexao()
        cur = con.cursor()

        sql = 'DELETE FROM playlists WHERE id = ?'

        cur.execute(sql, (id,))

        con.commit()
        con.close()

        print(f'Id {id} excluído com sucesso.')
        print("\n ---------------------------------- \n")
    if(m==5):
        musica_id = input('Música ID: ')
        playlist_id = input('Playlist ID: ')

        con = Banco.conexao()
        cur = con.cursor()

        sql = 'INSERT INTO musica_playlist VALUES (?, ?)'

        cur.execute(sql, (musica_id, playlist_id))

        con.commit()
        con.close()

        print(f'Música adicionada a playlist com sucesso.')
        print("\n ---------------------------------- \n")
