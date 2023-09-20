'''
import this
'''
first_name = input("Digite o primeiro nome: ")
middle_name = input("Digite o nome do meio: ")
last_name = input("Digite o ultimo nome: ")
age = int(input("Digite a idade: "))

# Concatenating strings
full_name = first_name + " " + middle_name + " " + last_name

# Making first letter as capital
print("Imprimindo o nome com iniciais maiusculas: " + full_name.title())

# making full word uppercase
print("Imprimindo o nome com letras maiusculas: " + full_name.upper())

# making full worl lower case
print("Imprimindo o nome com letras minusculas: " + full_name.lower())

# converting int to str
print("Imprimindo dados completos: " + full_name.title() + " has " + str(age) + " years old")

# tab
print("\tgregory")

# new line
print("\ngregory")

# removing space from the left side
favorite_language = '                       python'
print(favorite_language)
print(favorite_language.lstrip())

# removing space from the right side
favorite_language = 'python              '
print(favorite_language)
print(favorite_language.rstrip())

# removing space from the both sides
favorite_language = '                       python                '
print(favorite_language)
print(favorite_language.strip())

print(0.2 + 0.1)

name = "gregory"
middle_name = "da costa"
last_name = "moser"
age = 31

print("o tipo da idade é: " + str(type(age)))

if type(age) == int:
    print(type(age))
else:
    print("not int")

age_em_texto = str(age)

print("o tipo da idade agora é: " + str(type(age_em_texto)))

if type(age_em_texto) == int:
    print(type(age))
else:
    print("not int")