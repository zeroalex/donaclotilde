from model import * 
madruguinha = Model()



#listar tudo
data = madruguinha.list_all()
print(data)


"""
#realizar busca simples -list_filter
print("search: ")
busca=input()
data = madruguinha.list_filter(busca )

for x in data:
	print(x)

"""


"""
#realizar busca para contagem - 
print("search: ")
busca=input()
count = madruguinha.list_count(busca)
print(count)

"""

"""
#realizar busca complexa -list_filter_where
print("search: ")
busca=input()
data = madruguinha.list_filter_where(busca )

for x in data:
	print(x)

"""



"""
#salvar simples
base={}

print("cadastrar")
print('name: ')
base['name']=input()

print('adress: ')
base['adress']=input()
print('number: ')
base['number']=input()
print('password: ')
base['password']=input()

madruguinha.save(base)

data = madruguinha.list_all()
print(data)
"""

"""
#salvar simples

base={}

base['name']="incluido"

base['adress']="asdasd"

base['number']="sdsdgsd"

base['password']="234234"
base['last']="asdasd"

madruguinha.save(base)

data = madruguinha.list_all()
print(data)

"""
"""
#updadte

base={}

base['name']="midificado"

base['adress']=" modificado"

madruguinha.update(base)

data = madruguinha.list_all()
print(data)

"""

"""

asd=[x for x in madruguinha.map.values()]
print(asd)
"""

