print('Привет, напиши разные целые числа:')
first, second, third = int(input('1: ')), int(input('2: ')), int(input('3 '))

if first == second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')