import sqlite3



def criar_db():
        # conectando...
        conn = sqlite3.connect('database.db')
        # definindo um cursor
        cursor = conn.cursor()

        # criando a tabela (schema)
        cursor.execute("""
        CREATE TABLE database (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                idexterno INTEGER,
                numero TEXT NOT NULL,
                cor     VARCHAR(111) NOT NULL,
                
                criado_em DATE NOT NULL
        );
        """)

        print('Tabela criada com sucesso.')
        # desconectando...
        conn.close()

print("asd")


"""
Controle de data base via json e configuração

a ideia é conseguir gerenciar e implementar as açoes 
de db atraves das configurações do json

as acoes possiveis são as seguintes

- criar tabela
- modificar tabela
- apagar tabela

- implementar relacionamento de tabelas


"""