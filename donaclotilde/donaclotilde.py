import sqlite3

#camada de abstração para db SQLITE e python
#movendo pedras

print ("ola madruguinha!")

class Donaclotilde:
    def __init__(self,):
        self.entrada_select=[]
        self.entrada_from_table=[]
        self.entrada_where=[]
        self.entrada_insert=[]
        self.query=[]

    def connect_db(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def select(self,kwargs):
        data= kwargs

        if type(data) is list:
            for x in data:
                if self.entrada_select:
                    self.entrada_select.append(" , ")
        
                self.entrada_select.append(x)
        else:
            if self.entrada_select:
                self.entrada_select.append(" , ")
            self.entrada_select.append(data)

    def where(self,busca, coluna, filtro='LIKE'):

        self.entrada_where.append("WHERE")

        self.entrada_where.append(coluna)
        self.entrada_where.append(filtro)
        if filtro=='LIKE':
            self.entrada_where.append('"%'+busca+'%"')
        else:
            self.entrada_where.append('"'+busca+'"')
    def where_combining(self, busca, coluna, operator, filtro='LIKE'):
        
        self.entrada_where.append(operator)
        self.entrada_where.append(coluna)
        self.entrada_where.append(filtro)
        if filtro=='LIKE':
            self.entrada_where.append('"%'+busca+'%"')
        else:
            self.entrada_where.append('"'+busca+'"')
        


    def from_table(self,kwargs):
        data= kwargs
        if not self.entrada_from_table:
            self.entrada_from_table.append("FROM")
        
        if type(data) is list:
            for x in data:
                self.entrada_from_table.append(x)
        else:
            self.entrada_from_table.append(data)


    def result_list(self,kwargs):
        sql = kwargs
        self.connect_db()
        self.cursor.execute(sql)
        dados=self.cursor.fetchall()
        self.conn.close()

        return dados


        
    def result_dict(self,kwargs):
        sql = kwargs
        self.connect_db()
        self.cursor.execute(sql)
        dados=self.cursor.fetchall()
        self.conn.close()

        return dados
    

    def get(self):
        self.query.append("SELECT")
        if self.entrada_select:
            for x in self.entrada_select:
                self.query.append(x)
        if self.entrada_from_table:
            for x in self.entrada_from_table:
                self.query.append(x)
        data = self.query
        if self.entrada_where:
            print(self.entrada_where)
            for x in self.entrada_where:
                self.query.append(x)
        data = self.query

        self.entrada_select=[]
        self.entrada_from_table=[]
        self.entrada_insert=[]
        self.entrada_where=[]
        self.query=[]
        
        sql=self.turn_sql_string(data)
            
        return sql

    def set(self,tabela,valores,colunas):
        
        self.entrada_insert.append("INSERT INTO")
        
        self.entrada_insert.append(tabela)
        self.entrada_insert.append("(")
        
        for x in colunas:
            self.entrada_insert.append(x)
            self.entrada_insert.append(" , ")
        self.entrada_insert.pop()
        self.entrada_insert.append(")")

        self.entrada_insert.append("VALUES")
        self.entrada_insert.append("(")
        
        for x in valores:
            self.entrada_insert.append(' " '+x+' " ')
            self.entrada_insert.append(" , ")
        self.entrada_insert.pop()
    
        self.entrada_insert.append(")")


        data = self.entrada_insert

        self.entrada_select=[]
        self.entrada_from_table=[]
        self.entrada_insert=[]
        self.entrada_where=[]
        self.query=[]
        
        sql=self.turn_sql_string(data)
        return sql
        
        
    def insert(self,kwargs):
        sql=kwargs
        self.connect_db()
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

        
    def turn_sql_string(self,kwargs):
        sql=''
        for palavra in kwargs:
            sql=sql+" "+palavra
        return sql
