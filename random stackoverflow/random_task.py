import random

data_lists = [[], [], [], []]

for k in data_lists:
    name = input('Whats your name: ')
    number = int(input('one number: '))
    age = int(input('Other number: '))

    k.append(name + " " + str(number) + " " + str(age))

random.shuffle(data_lists)

print(data_lists[0])
print(data_lists[1])
print(data_lists[2])
print(data_lists[3])
