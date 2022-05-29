#!/usr/bin/python
# -*- coding: latin-1 -*-

import sqlite3

class Donaclotilde:
    def __init__(self,):
        
        self.entrada_select=[]
        self.entrada_count=[]
        self.entrada_from_table=[]
        self.entrada_where=[]
        self.entrada_insert=[]
        self.query=[]
    

    def connect_db(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def select(self,kwargs):
        self.entrada_select.append(kwargs)
        

    def count(self,kwargs):
        self.entrada_count.append(kwargs)


    def where(self,busca, coluna, operator='LIKE', sign='any'):
        

        """     
        WHERE ContactName LIKE 'a%o'    Finds any values that start with "a" and ends with 
        """


        self.entrada_where.append(coluna)
        self.entrada_where.append(operator)
        
        if operator=='LIKE':
            if sign=='any': self.entrada_where.append('"%'+busca+'%"')
            if sign=='start': self.entrada_where.append('"'+busca+'%"')
            if sign=='end': self.entrada_where.append('"%'+busca+'"')
            if sign=='second': self.entrada_where.append('"_'+busca+'%"')
            if sign=='least2': self.entrada_where.append('"'+busca+'_%"')
            if sign=='least3': self.entrada_where.append('"'+busca+'__%"')

        else:
            self.entrada_where.append('"'+str(busca)+'"')


    def where_combining(self, operator):
        
        self.entrada_where.append(operator)
        

    def from_table(self,kwargs):
        
        self.entrada_from_table.append(kwargs)


    def result_list(self,sql):
        
        

        self.connect_db()
        
        self.cursor.execute(sql)
        dados=self.cursor.fetchall()
        self.conn.close()
        
        #print(dados)
        
        lista=[list(x) for x in dados]
                
        return lista

    def result_first(self,sql):

        self.connect_db()
        
        self.cursor.execute(sql)
        dado=self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
             
        return dado
 
    def limit(self,kwargs):
        #falta
        pass
    def order(self,kwargs):
        #escrever se é crescente ou decresente


        pass

        
    def result_dict(self,sql):

        self.connect_db()
        self.cursor.execute(sql)
        dados=self.cursor.fetchall()
        self.conn.close()

        return dados
    

    def get(self):
        
        if self.entrada_select!=[]: self.query.append('SELECT '+ ' , '.join(self.entrada_select))

        if self.entrada_count!=[]: self.query.append('SELECT COUNT ('+ ' , '.join(self.entrada_count)+')')

        self.query.append('FROM '+ ' , '.join(self.entrada_from_table))
        
        if self.entrada_where!=[]: self.query.append( 'WHERE '+ ' '.join(self.entrada_where))
        
        print(self.entrada_where)
        data = self.query
        
        print(data)
        self.entrada_select=[]
        self.entrada_count=[]
        self.entrada_from_table=[]
        self.entrada_insert=[]
        self.entrada_where=[]
        self.query=[]
        
        sql=self.turn_sql_string(data)
        print(sql)    
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
            self.entrada_insert.append(' "'+x+'" ')
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
    def setup(self,tabela,valores,colunas):
        
        self.entrada_insert.append("UPDATE")
        
        self.entrada_insert.append(tabela)
        self.entrada_insert.append("SET")
        self.entrada_insert.append("(")
        
        for x in colunas:
            self.entrada_insert.append(' "'+x+'" ')
            self.entrada_insert.append(" , ")
        self.entrada_insert.pop()
        self.entrada_insert.append(")")

        self.entrada_insert.append("=")
        self.entrada_insert.append("(")
        
        for x in valores:
            self.entrada_insert.append(' "'+x+'" ')
            self.entrada_insert.append(" , ")
        self.entrada_insert.pop()
    
        self.entrada_insert.append(")")

        if self.entrada_where:
        
            for x in self.entrada_where:
                self.entrada_insert.append(x)
        


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
    def update(self,kwargs):
        sql=kwargs
        self.connect_db()
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

        
    def turn_sql_string(self,kwargs):
        sql=' '.join(kwargs)
        return sql