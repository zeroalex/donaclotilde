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
		

	def connect_db(self):
		self.conn = sqlite3.connect('database.db')
		self.cursor = self.conn.cursor()


	def save(self,kwargs):
		
		values=[]
		for x in kwargs.values():
			values.append(x)
		
		columns=[]
		for x in kwargs.keys():
			columns.append(x)

		sql = self.set("user",values,columns)
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
			self.where("sta","name","=")

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
		



