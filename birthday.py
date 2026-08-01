birthdays = {'rabi' : '4 May', 'gobinda' : '13 March', 'Bablu' : '28 April', 'Dhrub' : '31 May'}

while True:
    print('Please Enter Name')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information of ' + name)
        print('What is there birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday databases updated.')

for i in birthdays.keys():
    print(i)
for i in birthdays.values():
    print(i)
for i in birthdays.items():
    print(i)
