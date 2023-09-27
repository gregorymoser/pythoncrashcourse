
# creating a list
# A list is a collection of items in a particular order
bicycles = ['trek','cannondale', 'redline','specialized']
print(bicycles)

# accessing element in a certain position in the list
print(bicycles[2])
print(bicycles[-1])
print(bicycles[3].title())

# concatenating list element with string in a message
message = "my first bicycle was " + bicycles[3].upper() + "."
print(message)

# adding element to the end of the list
bicycles.append('Cross')
message = "my last bicycle is a " + bicycles[4] + ".\n"
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'Ducati'
print(motorcycles)

# manually changing elements positions in list
motorcycles.append('Honda')
print(motorcycles)
temp = motorcycles[-1]
motorcycles[-1] = motorcycles[0]
motorcycles[0] = temp
print(motorcycles[0].title())
print(motorcycles)

# inserting the element into desired position
motorcycles.insert(2, 'BMW')
print(motorcycles)

# deleting element of known position
del motorcycles[4]
print(motorcycles)

# deleting element using pop method
popped_motorcycles = motorcycles.pop()
print(motorcycles)

# printing the removed element with pop
print(popped_motorcycles)

last_owned = motorcycles.pop()
print('Last motorcycle owned is ' + last_owned.upper() + '.')

# using pop to remove elements in a specific position from the list
motorcycles2 = ['suzuki', 'Kawasaki', 'BMW', 'Ducati', 'Yamaha', 'Honda']
first_owned = motorcycles2.pop(0)
print('First motorcycle owned was: ' + first_owned.title() + '.')

# Removing an item according to the element, without knowing the position
motorcycles2.remove('Yamaha')
print(motorcycles2)

# removing element and explaining why
too_expensive = 'Ducati'
motorcycles2.remove(too_expensive)
print('\nRemoving ' + too_expensive.title() + ' as this is too expensive for me')
print(motorcycles2)

# do it yourself

print('\n-----------------------------')
print('-----Lista de convidados-----\n')
guest1 = input('Digite o nome do primeiro convidado: ')
guest2 = input('Digite o nome do segundo convidado: ')
guest3 = input('Digite o nome do terceiro convidado: ')

convidados = [guest1.title(), guest2.title(), guest3.title()]
print('\nLista de convidados até o momento abaixo: ')
print(convidados)

absent = input('\nDigite o nome do convidado que nao podera comparecer: ')
position = convidados.index(absent)

replaced_guest = input('Digite o nome do convidado subtituto: ')
convidados.insert(position, replaced_guest.title())

convidados.remove(absent)
print('\nO convidado ' + absent.title() + ' nao podera comparecer')
print('Em seu lugar, o convidado ' + replaced_guest.title() + ' foi adicionado a lista.')

print('\nLista de convidados até o momento abaixo: ')
print(convidados)

print('\n-----Mesa maior disponível!-----\n')
convidados.insert(0, input('Digite o nome do primeiro novo convidado no comeco da lista: '))
convidados.insert(1, input('Digite o nome do segundo novo convidado no comeco da lista: '))
convidados.append(input('Digite o nome do terceiro novo convidado no final da lista: '))


print('\nLista de convidados até o momento abaixo: ')
print(convidados)

print('\n-----Mesa maior indisponível!-----\n')

# sorting the guest list alphabetically
convidados.sort()
print(convidados)

first_name = input('Type the first name: ')
middle_name = input('Type the second name: ')
last_name = input('Type the third name: ')

full_name = [first_name.title(), middle_name.title(), last_name.title()]
print(full_name)

cars = ['volvo', 'bmw', 'mercedes', 'tesla', 'honda', 'porshe']
cars.sort()
print(cars)

# sorting in descending order
cars.sort(reverse=True)
print(cars)

# sorted method
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# reverse list
print("\nHere is the reversed list:")
cars.reverse()
print(cars)

# to find out the list size
print(len(cars))

# for loop for list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)