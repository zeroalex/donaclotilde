#!/usr/bin/python
# -*- coding: latin-1 -*-

#model usado como exemplo, suas consultas devem ser construidas conforme sua necessidade

from donaclotilde import *

from datetime import date
import sqlite3


class Model(Donaclotilde):
	"""docstring for Model"""
	def __init__(self):
		#super(Model, self).__init__()
		#self.arg = argi
		self.usuario="defalt"
		self.entrada_select=[]
		self.entrada_from_table=[]
		self.entrada_insert=[]
		self.entrada_count=[]
		self.entrada_where=[]
		self.query=[]


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

	def list_filter(self,search):
		
		#self.select('id')
		self.select('name')
		self.select('adress')
		self.select('number')
		self.select('password')
		self.select('last')
		
		self.from_table("user")
		if search:
			self.where(search,"name")
			
		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass



