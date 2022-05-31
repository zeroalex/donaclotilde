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
        
    def clear_vars(self):
        self.entrada_select=[]
        self.entrada_count=[]
        self.entrada_from_table=[]
        self.entrada_insert=[]
        self.entrada_where=[]
        self.query=[]
        

    def select(self,kwargs):
        self.entrada_select.append(kwargs)
        

    def count(self,kwargs):
        self.entrada_count.append(kwargs)


    def where(self,search, column , operator='LIKE', sign='any'):
        

        self.entrada_where.append(column)
        self.entrada_where.append(operator)
        
        if operator=='LIKE':
            if sign=='any': self.entrada_where.append('"%'+search+'%"')
            if sign=='start': self.entrada_where.append('"'+search+'%"')
            if sign=='end': self.entrada_where.append('"%'+search+'"')
            if sign=='second': self.entrada_where.append('"_'+search+'%"')
            if sign=='least2': self.entrada_where.append('"'+search+'_%"')
            if sign=='least3': self.entrada_where.append('"'+search+'__%"')

        else:
            self.entrada_where.append('"'+str(search)+'"')


    def where_combining(self, operator):
        
        self.entrada_where.append(operator)
        

    def from_table(self,kwargs):
        
        self.entrada_from_table.append(kwargs)


    def result_list(self,sql):
        
        self.connect_db()        
        self.cursor.execute(sql)
        dados=self.cursor.fetchall()
        self.conn.close()

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
        
        
        sql=self.turn_sql_string(self.query)
        
        #print(data)
        self.clear_vars()
        
        print(sql)    
        return sql

    def set(self,tabela,valores,colunas):
        
        self.entrada_insert.append("INSERT INTO "+tabela+" ( "+ ' , '.join(colunas)+" ) ")
        
        self.entrada_insert.append("VALUES ( '" + "' , '".join(valores)+"' ) ")

        sql=self.turn_sql_string(self.entrada_insert)

        self.clear_vars()

        print(sql)
        return sql
    
    def setup(self,tabela,valores,colunas):
        
        self.entrada_insert.append("UPDATE "+tabela+" SET ( "+ ' , '.join(colunas)+" ) ")

        self.entrada_insert.append(" = ( '" + "' , '".join(valores)+"' ) ")

        if self.entrada_where!=[]: self.entrada_insert.append( 'WHERE '+ ' '.join(self.entrada_where))
        
        sql=self.turn_sql_string(self.entrada_insert)

        self.clear_vars()

        print(sql)
        return sql
        
        
    def insert(self,sql):
        
        self.connect_db()
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

    def update(self,sql):
        
        self.connect_db()
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

        
    def turn_sql_string(self,kwargs):
        sql=' '.join(kwargs)
        return sql
