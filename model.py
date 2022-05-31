#!/usr/bin/python
# -*- coding: latin-1 -*-

#model usado como exemplo, suas consultas devem ser construidas conforme sua necessidade

from donaclotilde import *

from datetime import date
import sqlite3



class Model(Donaclotilde):
	"""ATRIBUTOS DO Model HERDADOS DE Donaclotilde"""
	""" /entrada_select /entrada_count /entrada_from_table /entrada_where /entrada_insert /query """
	def __init__(self):
		super().__init__()
		self.map={}
		self.map['user'] = [
			["id", "inter key "],
			["name", "string"],
			["name", "string"],
			["name", "string"],
		]
		
		"""
		talves proximo passso, declarar os valores do banco de dados em um dicionario no model
		dessa forma controlar e mapear db automaticamente no codigo
		desenvolver exemplo acima para melhor aprimorar o conceito gradativamente

		self.map[''] = "user"
		self.map['TABLE'] = "user"
		"""

	def connect_db(self):
		self.conn = sqlite3.connect('database.db')
		self.cursor = self.conn.cursor()


	def save(self,kwargs):
		
		values=[x for x in kwargs.values()]
		columns=[x for x in kwargs.keys()]
		
		sql = self.set("user",values,columns)
		#print(sql)
		self.insert(sql)

	def update(self,kwargs):
		
		values=[x for x in kwargs.values()]
		columns=[x for x in kwargs.keys()]
		
		self.where( 5 ,"id","=")
		
		sql = self.setup("user",values,columns)
		#print(sql)
		self.insert(sql)

	def list_all(self):

		self.select('*')
		
		self.from_table("user")
		
		sql = self.get()
		data = self.result_list(sql)
		return data



	def list_filter(self,search=None, coluna=None):
		
		#self.select('id')
		self.select('name')

		if coluna:
			self.select('adress')
		#self.select('number')
		self.select('password')
		#self.select('last')
		
		self.from_table("user")

		if search:
			self.where(search,"name")
			self.where_combining("AND")
			self.where("Josef Stalin","name","=")

		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass

	def list_filter_where(self,search=None, id=1):
		
		#self.select('id')
		self.select('name')
		self.select('adress')
		#self.select('number')
		self.select('password')
		#self.select('last')
		
		self.from_table("user")

		if search:
			self.where(search,"name","LIKE","start")
			self.where_combining("AND")
			self.where_combining("(")

			self.where( id ,"id","=")
			self.where_combining("OR")
			self.where( "321" ,"password","=")

			self.where_combining(")")


		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass

	def list_count(self, search):
		
		self.count('*')
		
		self.from_table("user")

		if search:
			self.where(search,"name")
			
			self.where_combining("OR")
			self.where("sta","name")
			
		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass
		



