#nome, nunmero,cor
import json 
from model import *

class Data(Model):
	def __init__(self):
		self.nome=""
		self.numero=""
		self.cor=""

	def record(self):
		pass
	def showlists(self):
		#pode ser substituido por uma interface
		

		pass	
		
	def recordlocal(self):
		#grava em formato de texto
		conteudo = '{ "nome": "'+self.nome+'","numero":"'+self.numero+'", "cor" :"'+self.cor+'"}'
		dados = open('database/'+self.nome+'.json','w')
		dados.write(conteudo)
		dados.close()

	def selectdel(self):
		#menu completo para filtros, buscar, ordenar
		#talves usar para casos de del, up, e show1

		delete=input("qual a deletar: ")
		self.delete=delete


		pass

	def insert(self):
		#pode ser substituido por uma interface
		nome=input("qual nome: ")
		self.nome=nome
		numero=input("qual numero: ")
		self.numero=numero
		cor=input("qual cor: ")
		self.cor=cor
	

		#self.recordlocal()

	