# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Prints "Hello, World!" to the terminal window.
print("Hello, World!")

#hello me
print("Hello_Me!")

#humpty_dumpty
print("Humpty Dumpty sat on a wall,")
print("Humpty Dumpty had a great fall.")
print("All the king's horses and all the king's men")
print("Couldn't put Humpty together again.")

#hello others
print("Hello, Ted!")
print("Hello, Changdong!")
print("Hello, Zilan!")

#Self introduce
print("""Payne Wu
25
1.70
""")

#Two_numbers
print("13 + 22 =", 13 + 22)
print("22 - 13 =", 22 - 13)
print("13 * 22 =", 13 * 22)
print("22 / 13 =", 22 / 13)
print("22 // 13 =", 22 // 13)
print("22 % 13 =", 22 % 13)

#Coding-hours
workdays = 5
coding_hours = workdays * 17 * 6
print("Total coding hours are " + str(coding_hours))

percentage = 52 * 17 / coding_hours
print("The percentage is " + str(percentage))

#Favorite number
favorite_number = 43
print("My favorite number is: " + str(favorite_number))

#swap
a = 123
b = 526
a, b = b, a
#c = a, a = b, b = c
print(a)
print(b)

#bmi
massInKg = 81.2
heightInM = 1.78
BMI = massInKg / heightInM ** 2
print("BMI is: " + str(BMI))

#define basic info
name = "Peiwen Wu"
age = 25
height = 1.70
married = False
print(name)
print(age)
print(height)
print(married)

#Value Mutation
a = 3
a += 10
print(a)

b = 100
b -= 7
print(b)

c = 44
c *= 2
print(c)

d = 125
d /= 5
print(d)

e = 8
e **= 3
print(e)

f1 = 123
f2 = 345
if f1 > f2: print("True")
else: print("False")

g1 = 350
g2 = 200
g2 *= 2 
if g2 > g1: print("True")
else: print("False")

h = 1357988018575474
mod = h % 11
if mod == 0: print("11 is a divisor of h = " + str(h))
else: print("11 is not a divisor of h = " + str(h))

i1 = 10;
i2 = 3;
if i1 > i2 **2 and i1 < i2 **3: print("True")
else: print("False")

j = 1521
mod_3 = j % 3
mod_5 = j % 5
if mod_3 == 0 or mod_5 ==0: print(str(j) + " is divisible by 3 or 5")
else: print(str(j) + " is not divisible by 3 or 5")

#cubiod
a = int(input("Please input the length of the cuboid: "))
b = int(input("Please input the widenth of the cuboid: "))
h = int(input("Please input the height of the cuboid: "))
surface = 2 * (a + b + h)
volume =  a * b * h
print("Surface Area: " + str(surface))
print("Volume: " + str(volume))

#Seconds in a day
current_hours = 14
current_minutes = 34
current_seconds = 42
seconds = (24 - current_hours) * 3600 + (60 - current_minutes) * 60 + 60 - current_seconds
print("The remaining seconds are " + str(seconds))

#Hello_user
print("Hello, what's your name?")

#mile to km converter
mile = int(input("Please input an integer distance in miles: "))
km = mile / 1000
print("The distance in km is " + str(km) + "km")

#Animals and legs
chicken = int(input("Please input the number of chickens: "))
pigs = int(input("Please input the number of pigs: "))
legs = chicken * 2 + pigs * 4
print("The number of legs is " + str(legs))

#Average of input
row = input("Please input 5 integers like a, b, c, d, e: ")
list_row = row.split(",")
sum = 0
for i in range(0, len(list_row), 1):
    sum = int(list_row[i]) +sum
average = sum / len(list_row)
print("Sum: " + str(sum))
print("Average: " +str(average))

#odd_even
num = int(input("Please input a number: "))
if num % 2 == 0: print("Even")
else: print("Odd")

#one two a lot
number = int(input("Please input an integer number: "))
if number <= 0: print("Not enough")
elif number == 1: print("One")
elif number == 2: print("Two")
elif number >= 2: print("A lot")
else: print("")

#Print bigger
num1 = [input("Please input two number: ") for i in range(2)]
if num1[0] > num1[1]: print("The bigger one is " + num1[0])
else: print("The bigger one is " + num1[1])

#Party indicator
girl = int(input("Please input the number of girls: "))
boy = int(input("Please input the number of boys: "))
if girl == 0: print("Sausage party")
elif girl + boy < 20: print("Average party")
elif girl + boy > 20 and girl != boy: print("Quite cool party")
else: print("The party is excellent!")

#Conditional variable mutation
a = 24
out = 0
if a % 2 == 0: out += 1
print(out)

b = 13
out2 = ""
if b < 10: out2 = "Less!"
elif b > 20: out2 = "More!"
else: out2 = "Sweet!"
print(out2)

c = 123
credits = 100
is_bonus = False
if is_bonus == True: c = c
elif credits < 50: c -= 2
else : c -= 1
print(c)

d = 8
time = 120
out3 = ""
if time % 4 != 0: out3 = "Run Forest Run"
elif time <= 200: out3 = "check"
else: out3 = "Time out"
print(out3)

#I wont cheat on the exams
for i in range(100): 
    print("I won't cheat on the exam!")

#Print Even
for i in range(0,500+1,2):
    print(str(i))

#Multiplication_table 
num_mult = int(input("Please input a integer number: "))
for i in range(1, 11):
    multiplication = i * num_mult
    print(str(i) + " * " + str(num_mult) + " = " + str(multiplication))

#Count from to 
num2 = [input("Please input two number: ") for i in range(2)]
if num2[1] <= num2[0]: print("The second number should be bigger")
else: 
    for i in range(0, int(num2[1]) - int(num2[0])):
      print(int(num2[0]) + i)

#Fizz buzz
for i in range(1, 100 + 1):
    if i % 3 == 0 and i % 5 == 0: print("Fizz and Buzz")
    elif i % 3 == 0: print("Fizz")
    elif i % 5 == 0: print("Buzz")
    else: print(str(i))
      
#Draw triangle
num3 = int(input("Please input a integer number: "))
star = ""
for i in range(0, num3):
    star = star + "*"
    print(str(star))

#Draw pyramid
num4 = int(input("Please input a odd number: "))
star2 = []
mid = (num4 + 1) // 2 - 1
for i in range(mid + 1):
    star2 = star2 + [" "]

firstline = " ".join(str(x) for x in star2)
print(firstline[::-1],"*",firstline)
for i in range(0, mid):
    star2[i] = "*"
    line = " ".join(str(x) for x in star2)
    print(line[::-1], "*", line)

#Draw diamond
num5 = int(input("Please input a odd number: "))
star = [" "] * num5
mid = (num5 + 1) // 2
blank = [" "] * (mid - 1)
firstline = " ".join(str(x) for x in blank)
print(firstline[::-1],"*",firstline)
for i in range(mid - 1):
    blank[i] = "*"
    strb = " ".join(str(x) for x in blank)
    print(strb[::-1],"*",strb)
dimond = ["*"] * (mid - 1)
for i in range(mid - 1):
    dimond[i] = " "
    strd = " ".join(str(x) for x in dimond)
    print(strd,"*",strd[::-1])

#Draw square
L = int(input("Please input the length of square: "))
t = "%" * L
m =  m = "%" + " " * (L - 2) + "%"
for i in range(L):
    if i == 0 or i == L - 1: print(t)
    else: print(m)
    
#Draw diagonal
L_diagonal = int(input("Please input the length of diagonal matrix: "))
for i in range(1, L_diagonal + 1):
    for j in range(1, L_diagonal + 1):
        if (i == 1 or i == L_diagonal or j == 1 or j == L_diagonal
            or i == j):
            print("%", end = "")
        else:
            print(" ", end = "")
    print()
print()
    
#Guess number
anwser = 43
inputnum = int(input("Please input an integer: "))
while anwser > 0:
    if inputnum > anwser: 
        print("The stored number is lower")
        inputnum = int(input("Please input an integer: "))
    elif inputnum < anwser: 
        print("The stored number is higher")
        inputnum = int(input("Please input an integer: "))
    else:
        print("You found the number: " + str(43)) 
        break

#Parametric_average
n_integer = int(input("Please input a number: "))
sum = 0
for i in range(n_integer):
    integer = int(input("Please input a integer: "))
    sum = sum + integer

average = sum / n_integer
print("Sun: " + str(sum))
print("Average: " + str(average))
    

#Creat a chess table
n_chess_table = 8
for i in range(1, n_chess_table + 1):
    if i % 2 != 0:
        print("% % % % ")
    else: print(" % % % %")
    print()
    
    
    
    
    
    
    



















