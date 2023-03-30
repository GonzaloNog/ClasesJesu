### Listas ###

my_list = list()
my_other_list = []

list = [1,1,3,4,5,6,7,8]

#print(list.count(1)) #cuenta la cantidad de veces que se repite un valor
#print(len(list))#cantidad de elementos

list_user = ['gonzalo', 'zeiss', 'gonza', 27]

name, lastname, apodo, ege = list_user

#print(lastname)

funtions_list = ['hola','chau','casa']

funtions_list.append('chau')#agrega al final

#print(funtions_list)

funtions_list.insert(2,'insert')#inserta en una posicion especifica

#print(funtions_list)

funtions_list.remove('chau')#elimina el primer elemento que encuentra

#print(funtions_list)

name = funtions_list.pop()

#print(name)

#print(funtions_list.pop())#retira el ultimo valor, se le puede pasar un idix

#print(funtions_list)

funtions_list_new = funtions_list.copy()#copia la lista

funtions_list_new.sort()#ordena la lista 

del funtions_list[1] #elimina el elemento sin retorno como con el pop()

#print(funtions_list)

funtions_list.clear() #borra todo el contenido de la lista

#print(funtions_list)
#print(funtions_list_new)

#Sets

my_set = set()
my_other_set = {}

#print(type(my_set))
#print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {'gonzalo','zeiss',27}
#print(type(my_other_set))

#print(len(my_other_set))

my_other_set.add('nog')

#print(my_other_set)#no es una estructura ordenada

my_other_set.add('nog')

print(my_other_set)#no se puede repetir un valor

print('nog' in my_other_set)
#print('noog' in my_other_set)

my_other_set.remove('nog')
#print(my_other_set)

my_other_set.clear()
#print(my_other_set)

del my_other_set

my_set = {'gonzalo','zeiss',27}

#my_list = list(my_set)
#print(my_list)
#print(my_list[0])

my_other_set = {'c++','c#','Python'}

my_new_set = my_set.union(my_other_set)

print(my_new_set)

print(my_new_set.difference(my_set))