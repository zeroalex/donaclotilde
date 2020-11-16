from datetime import date
import sqlite3
class Model:
	"""docstring for Model"""
	def __init__(self):
		#super(Model, self).__init__()
		#self.arg = argi
		pass
	def save(self):
		

		conn = sqlite3.connect('database.db')
		cursor = conn.cursor()

		data = date.today()
		cursor.execute("INSERT INTO usuario (nome, numero, cor, criado_em)VALUES (?,?,?,?)",(self.nome,self.numero,self.cor, data))

		conn.commit()

		print('Dados inseridos com sucesso.')

		conn.close()
		pass
	def listall(self):
		#lista somente os visivel verdadeiro
		conn = sqlite3.connect('database.db')
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM usuario;")
		self.list=cursor.fetchall()
		for linha in self.list:
			print(linha)
		
		conn.close()
		pass
	def delet(self):
		data = date.today()

		conn = sqlite3.connect('database.db')
		cursor = conn.cursor()
			
		cursor.execute("UPDATE usuario SET visivel = ?, criado_em = ? WHERE id = ?", (False, data, self.delete))
		
		conn.commit()
		print('Dados atualizados com sucesso.')
		conn.close()
		pass
