import helper

x = int(input('input an integer: '))
y = int(input('input another integer: '))
value = int(input('what is the multiplication of these numbers? '))

if value == helper.mulitply(x, y):
    print('well done')
else:
    print('try again')

print(f'x*y: {x*y}')
