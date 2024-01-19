print("Inicio de programa")
import time
wait_time = 1 #ESPEPRA # SEGUNDOS
time.sleep(wait_time)


# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

#Let us use the print() and len() built-in functions. Print function takes unlimited number of arguments. An argument is a value which we can be passed or put inside the function parenthesis, see the example below.

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument


#Let us print and also find the length of the variables declared at the top:
# Printing the values stored in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#Declaring Multiple Variable in a Line
#Multiple variables can also be declared in one line:
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables. Example:
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set



#Data Types
#There are several data types in Python. To identify the data type we use the type built-in function.
#I would like to ask you to focus on understanding different data types very well. When it comes to programming, 
#it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is 
#related to data types. We will cover data types in more detail in their respective sections.

#Check Data types: To check the data type of certain data/variable we use the type Example:
# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it


#Check Data types: To check the data type of certain data/variable we use the type Example:
# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set


#Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do 
#arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. 
#If we concatenate a number with a string, the number should be first converted to a string. 
#We will talk about concatenation in String section.


# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']


#Number data types in Python:
#Integers: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
#Floating Point Numbers(Decimal numbers) Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
#Complex Numbers Example: 1 + j, 2 + 4j, 1 - 1j

#Exercises: Level 1
#Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
#Write a python comment saying 'Day 2: 30 Days of python programming'
print("Dia 2 --> Esto deberia ser un comentario") #Dia 2 programacion python esto es un comentario.

#Declare a first name variable and assign a value to it
numero = 999
#Declare a last name variable and assign a value to it
Apellido = 'Ojeda'
#Declare a full name variable and assign a value to it
Nombre_completo='Jose Alex'
#Declare a country variable and assign a value to it
Pais='Mexico'
#Declare a city variable and assign a value to it
Ciudad='Nuevo Leon'
#Declare an age variable and assign a value to it
Edad= 31
#Declare a year variable and assign a value to it
año = 2024
#Declare a variable is_married and assign a value to it
Estado_civil = 'Comprometido'
#Declare a variable is_true and assign a value to it
verdadero = True
#Declare a variable is_light_on and assign a value to it
liegro = True
#Declare multiple variable on one line
nombre, objeto, peso = 'cubo', True,12345

#Check the data type of all your variables using type() built-in function
print(type(numero))
print(type(Apellido))
print(type(Nombre_completo))
print(type(Pais))
print(type(Ciudad))
print(type(Edad))
print(type(año))
print(type(Estado_civil))
print(type(verdadero))
print(type(liegro))
print(type(nombre,objeto,peso))
#Using the len() built-in function, find the length of your first name
print("la cantidad de caracteres en mi nombre es: ", len(nombre))
#Compare the length of your first name and your last name
#Declare 5 as num_one and 4 as num_two
#Add num_one and num_two and assign the value to a variable total
#Subtract num_two from num_one and assign the value to a variable diff
#Multiply num_two and num_one and assign the value to a variable product
#Divide num_one by num_two and assign the value to a variable division
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
#Calculate num_one to the power of num_two and assign the value to a variable exp
#Find floor division of num_one by num_two and assign the value to a variable floor_division
#The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#Take radius as user input and calculate the area.
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

##aqui estas actualizado###

input("FIN DE PROGRAMA -> Presiona Enter para continuar")









