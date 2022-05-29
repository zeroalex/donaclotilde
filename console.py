from model import * 
madruguinha = Model()



data = madruguinha.list_all()
print(data)


busca=input()

count = madruguinha.list_count(busca)
print(count)

print("search: ")
busca=input()
data = madruguinha.list_filter(busca )

for x in data:
	print(x)


"""
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