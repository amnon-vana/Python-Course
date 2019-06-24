'''
print("Hello World")
name = input("Enter your name: ")
print ("Hello",name)
print (name.split())
print("your name is: {} last name is: {}". format(name.split()[0],name.split()[1]))
print(f'your name is: {name.split()[0]} last name is: {name.split()[1]}')


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f'{a} + {b} = {a+b:10}')
print(f'{a} - {b} = {a-b:10}')
print(f'{a} * {b} = {a*b:10.5f}')
print(f'{a} / {b} = {a/b:10.5f}')

print("{} * {} = {:10}". format(a,b,a*b))

a = 4.2343455
print(f'{a:10.3f}')



s = input("Enter string: ")
xa = s.count('a')
xb = s.count('b')

if xa > 0:
    print(f'a appears {xa}')
elif xb > 0:
    print(f'b appears {xb}')
else:
    print("no!")


age = int(input("Enter your age: "))
if age < 0:
    print("not burn")
elif age <= 3:
    print("baby")
elif age <= 12:
    print("child")
elif age <= 18:
    print("teenager")
else:
    print("grownup")


s = input("Enter exersize: ")
lst = s.split()
x = float(lst[0])
y = float(lst[2])

if lst[1] == '+':
    print(f'{x} + {y} = {x + y}')
elif lst[1] == '-':
        print(f'{x} - {y} = {x - y}')
elif lst[1] == '*':
        print(f'{x} * {y} = {x * y}')
elif lst[1] == '*':
        print(f'{x} / {y} = {x / y}')
elif lst[1] == '**':
        print(f'{x} ** {y} = {x ** y}')


nums = [1,2,5,-6,7,'bomb',9,3]
neg_sum = 0
pos_sum = 0
for num in nums:
    if num != 'bomb':
        if num > 0:
            pos_sum += num
        else:
            neg_sum += num
print(f'Positive sum of list: {pos_sum}')
print(f'Negative sum of list: {neg_sum}')



nums = [4,2,8,-6,7,10,3]
sum = 0
for num in nums:
    if num % 2 == 0:
        print(num)
    else:
        flag = 'End'
        break


if flag == 'End':
    print('Not all list numbers are even')
else:
    print('all list numbers are even')



matrix = [[10,22,36],[-4,25,63],[87,98,109]]
max = matrix[0][0]
for mylist in matrix:
    sum = 0
    for num in mylist:
        sum += num
        if num > max:
            max = num
    print(f'Sum of list: {sum}')

print(f'The biggest number is: {max}')
'''

matrix = [[6,9,20,33],[1],[4,8,10],[5,7,10,20]]
matrix_new = []
for mylist in matrix:
    mini_matrix = []
    for num in mylist:
        mini_matrix.append(num % 2 == 0)
    matrix_new.append(mini_matrix)

print(matrix_new)




