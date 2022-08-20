"""
#1) write a program to find sum of number

#Method 1
first_number = eval(input('Enter number1: '))
second_number = eval(input('Enter number2: '))
print(first_number+second_number)

#Method 2
sums = 0
i = 0
n = eval(input('Enter number: '))
while i<n+1:
    sums = sums+i
    i=i+1
print(sums)    

    
#output
Enter number1: 10
Enter number2: 20
30
Enter number: 5
15
"""


"""
#2)WAP to find the number is strong number or not

number = int(input('Enter Number: '))
temp_number = number
sums = 0
while temp_number>0:
    reminder=temp_number%10
    fact = 1
    i = 1
    
    while i<=reminder:
        fact=fact*i
        i=i+1
        
    print(fact)    
    sums=sums+fact    
    temp_number = temp_number//10
    
#print(sums)    
     
if number==sums:
    print("Given number is a strong number")
else:
    print("Given number is not a strong number")

#output
 ==================
Enter Number: 123
6
2
1
Given number is not a strong number

================== RESTART: C:/Users/nk22230/python/22july.py ==================
Enter Number: 145
120
24
1
Given number is a strong number    
"""


"""
#3)Python Program to Find the Square Root

number = int(input('Enter Number: '))
square_root = number**0.5
print(square_root)

#output
 ==================
Enter Number: 25
5.0

================== RESTART: C:/Users/nk22230/python/22july.py ==================
Enter Number: 81
9.0
"""


"""
#4)Python Program to Calculate the Area of a Triangle

base = int(input('Enter base of a triangle: '))
height = int(input('Enter height of a triangle: '))
Area_triangle = 0.5*base*height
print(Area_triangle)

#output
Enter base of a triangle: 10
Enter height of a triangle: 10
50.0
"""


"""
#5)Python Program to Solve Quadratic Equation

a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))
#quadratic equation = a*(x**2)+b*x+c
dis = (b**2)-4*a*c  #discriminant of a number

if dis==0:
    quad_sol = -b/2*a
    #print()
    print(quad_sol, quad_sol)
else:    
    quad_sol1 = (-b + (dis**0.5))/(2*a)
    quad_sol2 = (-b - (dis**0.5))/(2*a)
    #print()
    print(quad_sol1,quad_sol2)

#output
Enter a value: 1
Enter b value: 5
Enter c value: 6
-2.0 -3.0
"""


"""
#6)Python Program to Swap Two Variables

first_number = int(input('Enter a first value: '))
second_number = int(input('Enter a second value: '))
first_number, second_number = second_number, first_number

print(first_number,second_number)

#output
Enter a first value: 10
Enter a second value: 20
20 10
"""


"""
#7)Python Program to Convert Kilometres to Miles

distance_in_km = eval(input("Enter distance"))
km_to_miles = 0.621371*distance_in_km

print(km_to_miles)

#output
Enter distance 1
0.621371

========================================================================== RESTART: C:/Users/nk22230/python/22july.py ==========================================================================
Enter distance 5
3.106855
"""


"""
#8)Python Program to Check Leap Year

year = int(input("Enter year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Given year is a leap year")
        else:
            print('Not a leap year')
    else:
        print("Given year is a leap year")
        
else:
    print('Not a leap year')

#output
Enter year: 2000
Given year is a leap year

========================================================================== RESTART: C:/Users/nk22230/python/22july.py ==========================================================================
Enter year: 24
Given year is a leap year

========================================================================== RESTART: C:/Users/nk22230/python/22july.py ==========================================================================
Enter year: 100
Not a leap year    
"""



"""
#9)Python Program to Check Prime Number
number = int(input("Enter any number"))
count=0
for i in range(1,number+1):
    if number%i==0:
        count=count+1

if count==2:
    print("Given number is a prime number")
else:
    print("Given number is a not prime number")


#output
Enter any number 5
Given number is a prime number

========================================================================== RESTART: C:/Users/nk22230/python/22july.py ==========================================================================
Enter any number 9
Given number is a not prime number
"""


"""
#10)Python Program to Find the Factorial of a Number
number = int(input("Enter any number"))
fact=1
for i in range(1,number+1):
    fact=fact*i

print("Factorial of a",number,"is",fact)    

#output
Enter any number 5
Factorial of a 5 is 120

========================================================================== RESTART: C:/Users/nk22230/python/22july.py ==========================================================================
Enter any number 4
Factorial of a 4 is 24
"""



"""
#11)Python Program to Print the Fibonacci sequence
series_number = int(input("Enter any number"))
first_number = 0
second_number = 1
print(first_number, second_number, end=" ")
for i in range(1,series_number+1):
    thitd_number =first_number+second_number
    print(thitd_number, end=" ")
    first_number, second_number = second_number, thitd_number


#output
Enter any number5
0 1 1 2 3 5 8
"""


"""
#12)Python Program to Check Armstrong Number

number =int(input("Enter any number"))
temp=origional_number=number
count = 0
while number>0:
    reminder = number%10
    count = count+1
    number = number//10
#power = count    

sums=0
while temp>0:
    reminder = temp%10
    sums+= (reminder**count)
    temp = temp//10   
    
if sums==origional_number:
    print("It's a strong number")
else:
    print("Not a strong number")
    
#output
C:\Users\nk22230\python>python now1.py
Enter any number371
It's a strong number

C:\Users\nk22230\python>python now1.py
Enter any number1634
It's a strong number

C:\Users\nk22230\python>python now1.py
Enter any number123
Not a strong number    
"""   
  

  
"""    
#13)Python Program to Find Armstrong Number in an Interval 
def length_number(original_number):
    count = 0
    ls=[]
    while original_number > 0:
            count=count+1
            if original_number==0:
                break
            ls.append(original_number%10)
            original_number = original_number//10
    #print(count)  
    #print(ls)
    return ls,count
    
def amstrong_number(num):
    a,b=length_number(num)
    sums = 0
    #print(a)
    for i in a:
        sums+=i**b
    return sums


for i in range(0,1000):
    if amstrong_number(i)==i:
        print("Amstrong Number",i)
"""



"""
#14)sum of natural numbers

number = int(input("Enter number"))
sums = 0
for i in range(number+1):
    sums=sums+i
    
print(sums)   


sum_natural_number = (number * (number+1))/2
print(sum_natural_number) 

#output
Enter number4
10
10.0        
"""


"""
#15)Python Program to Find the Factors of a Number 

number = int(input("Enter number"))

for i in range(1,number+1):
	if number%i==0:
		print(i, end=",")
        
#output
Enter number6
1
2
3
6

C:\Users\nk22230\python>python now4.py
Enter number10
1
2
5
10

C:\Users\nk22230\python>python now4.py
Enter number10
1
2
5
10

Enter number987654321
1,3,9,17,51,153,289,867,2601,379721,1139163,3417489,6455257,19365771,58097313,109739369,329218107,987654321,        
"""



"""
decimal=int(input("Enter a number: "))
binary_decimal=[]
while(decimal>0):
    dig=decimal%2
    binary_decimal.append(dig)
    decimal=decimal//2
binary_decimal.reverse()
print("Binary Equivalent is: ")
for i in binary_decimal:
    print(i,end=" ")
    
#output
Binary Equivalent is:
1 1 0 0    
"""  


""" 
decimal=int(input("Enter a number: "))
octa_decimal=[]
while(n>0):
    dig=decimal%8
    octa_decimal.append(dig)
    decimal=decimal//8
octa_decimal.reverse()
print("Binary Equivalent is: ")
for i in octa_decimal:
    print(i,end=" ") 
#output
Binary Equivalent is:
7 2    
"""



"""
#16)Python Program to Convert Decimal to Binary, Octal and Hexadecimal 

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
  
decimal_number = int(input("Enter decimal value: "))
def decimalToHexadecimal(decimal):
    hexadecimal = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
  
    return hexadecimal
  
  

print("The hexadecimal form of", decimal_number,
      "is", decimalToHexadecimal(decimal_number))

#output
The hexadecimal form of 69 is 45    
The hexadecimal form of 286 is 11E  
"""







"""
#17)Python Program to Find LCM 

first_number, second_number = map(int,(input("Enter 2 numbers")).split(","))

if first_number>second_number:
    greatest = first_number
else:
    greatest = second_number
while True:    
    if (greatest%first_number==0) and (greatest%second_number==0):
        lcm = greatest
        break
    greatest+=1
    
print("lcm of two numbers is ",lcm)


#output
Enter 2 numbers10,12
lcm of two numbers is  60

Enter 2 numbers20,40
lcm of two numbers is  40
"""



"""
#18)hcf

first_number, second_number = map(int,(input("Enter 2 numbers")).split(","))
if first_number<second_number:
    smallest = first_number
else:
    smallest = second_number
while True:    
    if (first_number%smallest==0) and (second_number%smallest==0):
        hcf = smallest
        break
    smallest-=1

print("highest common factor is ",hcf)

#output
Enter 2 numbers10,12
highest common factor is  2

C:\Users\nk22230\python>python now6.py
Enter 2 numbers9,12
highest common factor is  3
"""






