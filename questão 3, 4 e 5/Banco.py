import sqlite3


def conexao():
    return sqlite3.connect('ipod.sqlite')

con = conexao()
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS musicas
    (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        nome    TEXT    NOT NULL,
        artista TEXT    NOT NULL,
        album   TEXT    NOT NULL,
        ano     INTEGER NOT NULL,
        arquivo TEXT    NOT NULL
    )
''')

con.commit()
con.close()

con = conexao()
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS playlists
    (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data TEXT NOT NULL
    )
''')

con.commit()
con.close()

con = conexao()
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS musica_playlist
    (
        musica_id   INTEGER NOT NULL REFERENCES musicas (id),
        playlist_id INTEGER NOT NULL REFERENCES playlists (id),
        PRIMARY KEY (musica_id, playlist_id)
    )
''')

con.commit()
con.close()