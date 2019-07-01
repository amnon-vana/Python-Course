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


matrix = [[6,9,20,33],[1],[4,8,10],[5,7,10,20]]
matrix_new = []
for mylist in matrix:
    mini_matrix = []
    for num in mylist:
        mini_matrix.append(num % 2 == 0)
    matrix_new.append(mini_matrix)

print(matrix_new)


x=100;y=501;z=5

x=1000;y=199;z=-10

x=155;y=301;z=2

for i in range(x,y,z):
    print(i)




mylist = [5,6,7,8,9,10,20,30,40,50,60,70,80]
for i in range(2,len(mylist),3):
    print (mylist[i])



burgers = ["a","b","c","d","e"]

for i in range(len(burgers)):
    print(burgers[i])

for i in range(len(burgers)-1,-1,-1):
    print(burgers[i])

for i in range(-1,-len(burgers)-1,-1):
    print(burgers[i])

avg = 0
i = sum = 0
while avg <= 0:
    x = int(input("Enter first number: "))
    if x >= 0:
        sum += x
        i += 1
    else:
        break
print(sum/i)

x = 1
while x != 0:
    x = int(input("Enter first number: "))
    for i in range(x):
        print(i)

numbers = [1,5,-6,2,55,0,'boom',44]
for num in numbers:
    if num == 'boom':
        break
    elif num < 0:
        continue
    else:
        for i in range(num):
            print(f"{i}",end=',')
        print("")

'''

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
while True:
    act = input("Enter one of +,-,*,/,Q: ")
    if act == "+":
        print(x+y)
    if act == "-":
        print(x-y)
    if act == "*":
        print(x*y)
    if act == "/":
        if y == 0:
            break
        print(x/y)
    if act == "q" or act == "Q":
        break
