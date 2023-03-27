#Primera clase Prints y tipos de datos

print("Hola mundo")

'''consultar tipo de dato 
print(type("Hola mundo")) #string
print(type(5)) #int
print(type(1.5)) #float
print(type(1 + 5j)) #complex
print(type(True)) #bool
print(type([1, 2, 3])) #List
print(type({'name': 'Gonzalo'})) #Dictionary
print(type({9.8, 3.14, 2.7})) #Set
print(type({9.8, 3.14, 2.7})) #tuple
'''
#Variables 

numero = 1
print(type(numero))
numero = 'hola'
print(type(numero))
numero = 1.1
print(type(numero))

numero = 1 + int("5")

print(numero)

#Len
nombre = "gonzalo "
print(len(nombre)) #Cuenta los caracteres

name, surname, alias, age = "Gonzalo", "Zeiss", "Gonza", 27

print(name)
print(surname)
print(alias)
print(age)

print(3 > 4)#Imprime True or False 

name = "hola \nchau" # \n Deja un renglon
name2 = "\tEste es un string con tabulacion" #Tam \t
print(name2)

name, surname, age = 'Gonzalo', 'Zeiss', 35

#print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age)) 
#print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age)) #%s string %d entero %f float
print(f'Mi nombre es {name} {surname} y mi edad es {age}')

#Desempaquetado de caracteres
lenguage = 'Pythont'
a, b, c, d, e, f, g = lenguage
print(a)
print(b)

#Division

lenguage_slice = lenguage[1:]
print(lenguage_slice)

#Reverse

lenguage_slice = lenguage[:: -1]
print(lenguage_slice)

name = '5'
#funciones

#print(lenguage.capitalize()) #primera letra en mayuscula
#print(lenguage.upper()) #Todo mayuscula
#rint(lenguage.count('t')) #cantidad de un tipo
#print(name.isnumeric()) #Es numerica
#print(lenguage.lower()) #minusculas
#print(lenguage.upper().isupper()) #mayuscula y compueba sie s mayuscula
print(lenguage.startswith("Py")) #revisa como arranca 





