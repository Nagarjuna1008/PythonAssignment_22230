'''
#1)Print First 10 natural numbers using while loop 
number = int(input("Enter the number: "))
i=1
while i<=number:
    print(i, end=" ")
    i+=1
    

#2)Calculate the sum of all numbers from 1 to a given number 
def sums_number(number):
    sums = 0
    for i in range(1,number+1):
        sums+=i
    return sums

print(sums_number(int(input("Enter the number: "))))  

#3)Write a program to print multiplication table of a given number
number = int(input("Enter the number: ")) 
i = 1
for i in range(11):
    print(number*i, end=" ")


#4)Display numbers from a list using loop 
list1 = [1,2,3,4,'a','hai']
for i in list1:
    print(i, end="") 



#5)Count the total number of digits in a number     
number = int(input("Enter the number: ")) 
count=0
while number>0:
    count+=1
    number = number//10
    
print("Total number of digits equal to ", count)   

#output
Enter the number: 123456
Total number of digits equal to  6



#6)Print list in reverse order using a loop
list1=list(map(int,input("").split(","))) 
ls1=[]
i=len(list1)-1
while i>-1:
    ls1.append(list1[i])
    i=i-1
print(ls1)

#output
[100, 30, 40, 60, 40, 10]    



#7)numbers from -10 to -1 using for loopDisplay  
for i in range(-10,0,1):
    print(i,end=" ")

#output-10 -9 -8 -7 -6 -5 -4 -3 -2 -1



#8)Use else block to display a message “Done” after successful execution of for loop 
number = int(input("Enter number: ")) 
for i in range(number):
    print(i)
else:
    print("Done")
    
#output
Enter number: 4
0
1
2
3
Done    



#9)Write a program to display all prime numbers within a range 
number = int(input("Enter number: ")) 
def prime_numbers(number1):
    count=0
    j=1
    while j<=number1+1:
        if number1%j==0:
            count+=1
        j+=1
    return count

for i in range(1,number+1):
    if prime_numbers(i)==2:
        print(i, end=" ")
        
#output
Enter number: 5
2 3 5
Enter number: 100
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97  



#10)Display Fibonacci series up to 10 terms 
number = int(input())
first_number=0
second_number=1
print(first_number,second_number, end=" ")
for i in range(number):
    third_number=first_number+second_number
    print(third_number,end=" ")
    first_number,second_number=second_number,third_number
    
#output
0 1 1 2 3 5 8 13 21 34    



#11)Find the factorial of a given number 
number = int(input('Enter number: '))
fact=1
for i in range(1,number+1):
    fact=fact*i
print(fact) 

#output
Enter number: 5
120   



#12)Reverse a given integer number
number = int(input('Enter number: '))
while number>0:
    print(number%10,end='')
    number=number//10

#output
Enter number: 123
321 



#13)Find the sum of the series upto n terms
number = int(input('Enter number: '))
print("series_sum= ", number*(number+1)/2) 

#output
Enter number: 10
series_sum=  55.0       



#14)Calculate the cube of all numbers from 1 to a given number 
number = int(input('Enter number: '))
for i in range(1,number+1):
    print(i**3, end=" ")
    
#output
Enter number: 10
1 8 27 64 125 216 343 512 729 1000



#15)Use a loop to display elements from a given list present at odd index positions 
list1 = list(map(int,input().split()))
i=1
while i<=len(list1)-1:
    if i%2!=0:
        print(list1[i], end=" ")
    i=i+1    
    
#output
10 20 30 40 50 69
20 40 69    


#16)Name the keyword which helps in writing code involves condition.
if else


#17)Write the syntax of simple if statement. 
if (condition):
    block of code
    
    
#18)Is there any limit of statement that can appear under an if block. 
No




#19)Write a program to check whether a person is eligible for voting or not. (accept age from user) 
age = int(input("Enter age")) 

if age>17:
    print("Eligible")
else:
    print("Not Eligible")
    
#output
Enter age18
Eligible    



#20)Write a program to check whether a number entered by user is even or odd
number = int(input('Enter number: '))

if number%2==0:
    print("Even")
else:
    print("Odd")
    
    
#21)a program Write to check whether a number is divisible by 7 or not 
number = int(input('Enter number: '))

if number%7==0:
    print("True")
else:
    print("False")


#22)Write a program to display "Hello" if a number entered by user is a multiple of five , 
# otherwise print "Bye".    
number = int(input('Enter number: '))

if number%5==0:
    print("Hello")
else:
    print("Bye")
   
    
#23)Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : 
"""
            Unit                                                     Price   

First 100 units                                               no charge 

Next 100 units                                              Rs 5 per unit 

After 200 units                                             Rs 10 per unit  
"""   

units = int(input('Enter units: '))
if units>0 and units<=100:
    print("no charge")
elif units>=101 and units<=200:
    print('charge=', (units-100)*5)
else:
    print('charge=', 500+(units-200)*10)
    
#output
Enter units: 20
no charge

C:\Users\nk22230\python>python 26july2022.py
Enter units: 150
charge= 250

C:\Users\nk22230\python>python 26july2022.py
Enter units: 350
charge= 2000

C:\Users\nk22230\python>python 26july2022.py
Enter units: 30
no charge
'''


"""
#24)Write a program to display the last digit of a number. 
number = int(input('Enter number: '))
if number>0:
    print(number%10)
    
#output
Enter number: 15678
8    



#25)Write a program to check whether the last digit of a number( entered by user ) is  
#divisible by 3 or not. 
number = int(input('Enter number: '))
if number>0:
    rem=number%10
    if rem%3==0:
        print("Last digit divisible by 3")
    else:
        print("no")
  
#output  
Enter number: 124
no
Enter number: 123
Last digit divisible by 3 
"""



"""
#26)Write a program to accept percentage from the user and display the grade according to the following criteria: 

 

        Marks                                    Grade 

         > 90                                         A 

         > 80 and <= 90                       B 

        >= 60 and <= 80                       C 

         below 60                                  D        

percentage = int(input("Enter percentage: ")) 
if percentage>90 and percentage<=100:
    print("A")
elif percentage<=90 and percentage>80:
    print("B")
elif percentage<=80 and percentage>=60:
    print("C")
else:
    print("D")

#output 
Enter percentage: 90
B   
Enter percentage: 100
A
"""


"""
#27)Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria : 

     

        Cost price (in Rs)                                       Tax 

        > 100000                                                  15 % 

        > 50000 and <= 100000                          10% 

        <= 50000                                                  5% 

cost_price = int(input("Enter cost price: "))
if cost_price>100000:
    print("Road Tax to be paid is Rs.",(15/100)*cost_price)
elif cost_price<=100000 and cost_price>50000:
    print("Road Tax to be paid is Rs.",(10/100)*cost_price)
else:
    print("Road Tax to be paid is Rs.",(5/100)*cost_price)

#output 
Enter cost price: 100001
Road Tax to be paid is Rs. 15000.15  
Enter cost price: 100000
Road Tax to be paid is Rs. 10000.0   
"""


"""
#28)Write a program to check whether an years is leap year or not. 
year = int(input())
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")

#output
24
Leap Year

C:\Users\nk22230\python>python now2.py
2000
Leap Year

C:\Users\nk22230\python>python now2.py
1900
Not a Leap Year    
"""


#29)Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on. 
num = int(input())
dict1 = {1:'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
print(dict1[num])

C:\Users\nk22230\python>python now1.py
1
Sunday

C:\Users\nk22230\python>python now1.py
7
Saturday


#30)Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on 
num = int(input())
dict1 = {1:'January, 30 days', 2: 'February and 28 days', 3: 'March and 31 days', 4: 'April and 30 days',
        5: 'May and 31 days', 6: 'June and 30 days', 7: 'July and 31 days', 8: 'August and 31 days',
        9: 'September and 30 days', 10: 'October and 31 days', 11: 'November and 30 days', 12: 'December and 31 days',
        }
print(dict1[num])

1
January, 30 days
12
December and 31 days


#31)What do you mean by statement? 
A statement is an instruction that a Python interpreter can execute. So, in simple words, we can say anything written in Python is a statement

#32)Write the logical expression for the following: 
#A is greater than B and C is greater than D 
if A>B and C>D:




#33)Accept any city from the user and display monument of that city. 
'''
                  City                                 Monument 

                  Delhi                               Red Fort 

                  Agra                                Taj Mahal 

                  Jaipur                              Jal Mahal 
'''                 
City = input("Enter your city: ")                  
dict1 = {'Delhi':'Red Fort', 'Agra': 'Taj Mahal', 'Jaipur': 'Jal Mahal'} 
print(dict1[City])       

C:\Users\nk22230\python>python now1.py
Enter your city: Delhi
Red Fort

C:\Users\nk22230\python>python now1.py
Enter your city: Agra
Taj Mahal


#34)Write the output of the following if a = 9 

         

    if (a > 5 and a <=10):     

         print("Hello")     

           else:     

        print("Bye")

o/p: Hello


#35)Write a program to check whether a number entered is three digit number or not. 
num = int(input())
count=0
while num>0:
    rem = num%10
    count+=1
    num=num//10

if count==3:
    print("given number is a 3 digits number") 
else:
        print("No")
        
C:\Users\nk22230\python>python now1.py
123
given number is a 3 digits number 

C:\Users\nk22230\python>python now1.py
1234
No

#36)Write a program to check whether a person is eligible for voting or not.(voting age >=18)              
age = int(input("Enter age")) 

if age>17:
    print("Eligible")
else:
    print("Not Eligible")
    
#output
Enter age18
Eligible

#37)Write a program to check whether a person is senior citizen or not. 
age = int(input("Enter age")) 

if age>60:
    print("Senior citizen")
else:
    print("No")
    
C:\Users\nk22230\python>python now1.py
Enter age20
No

C:\Users\nk22230\python>python now1.py
Enter age65
Senior citizen    


#38)Write a program to find the lowest number out of two numbers excepted from user. 
num1 = int(input())
num2 = int(input())

if num1<num2:
    print(num1, 'is the smallest')
else:
    print(num2, 'is the smallest') 
    
C:\Users\nk22230\python>python now1.py
10
20
10 is the smallest

#39)Write a program to find the largest number out of two numbers excepted from user. 
num1 = int(input())
num2 = int(input())

if num1>num2:
    print(num1, 'is the gratest')
else:
    print(num2, 'is the gratest') 

C:\Users\nk22230\python>python now1.py
10
40
40 is the gratest    


#40)Write a program to check whether a number (accepted from user) is positive or negative. 
num = int(input())
if num>=0:
    print("positive number")
else:
    print("Negative number") 

C:\Users\nk22230\python>python now1.py
0
positive number

C:\Users\nk22230\python>python now1.py
5
positive number

C:\Users\nk22230\python>python now1.py
-2
Negative number  



#41)Write a program to check whether a number is even or odd. 
num = int(input())
if num%2==0:
    print("even")
else:
    print("odd")  

C:\Users\nk22230\python>python now1.py
0
even

C:\Users\nk22230\python>python now1.py
4
even

C:\Users\nk22230\python>python now1.py
99
odd    


#42)Write a program to whether a number (accepted from user) is divisible by 2 and 3 both. 
num = int(input())
if num%2==0 and num%3==0:
    print(num,'divisable by 2 and 3')
else:
    print("not divisible by 2 and 3")

C:\Users\nk22230\python>python now1.py
6
6 divisable by 2 and 3

C:\Users\nk22230\python>python now1.py
10
not divisible by 2 and 3    


#43)Write a program to find the largest number out of three numbers excepted from user. 
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1>num2 and num1>num3:
    print(num1, "is Bigger")
elif num2>num3:
    print(num2, "is Bigger")
else:
    print(num3, "is Bigger")
    

C:\Users\nk22230\python>python now1.py
10
40
30
40 is Bigger

C:\Users\nk22230\python>python now1.py
1
0
-7
1 is Bigger 



#44)#Accept the temperature in degree Celsius of water and check whether it is boiling or not (boiling point of water in 100 oC. 
temperature = int(input())
if temperature>65 and temperature<110:
    print("Water is boiling")
else:
    print("Wait for some time") 


100
Water is boiling

C:\Users\nk22230\python>python now1.py
40
Wait for some time    


#45)Accept the age of 4 people and display the youngest one and oldest one?
list1 = list(map(int,input().split(",")))
min_number = list1[0]
for i in list1:
    if i<min_number:
        min_number=i
print(min_number)        

max_number = list1[0]
for i in list1:
    if i>max_number:
        max_number=i
print(max_number)

10,20,30,40
10
40  


'''
#46)Accept the following from the user and calculate the percentage of class attended: 

 

a.     Total number of working days 

 

b.     Total number of days for absent 

 

    After calculating percentage show that, If the percentage is less than 75, than student will not be able to sit in exam. 
'''   
working_days = int(input()) 
absent_days = int(input())
present_days = working_days-absent_days

percentage =  (present_days/working_days)*100

if percentage>=75:
    print("Eligable for exam")
else:
    print("Not Eligable for exam")
    
    
C:\Users\nk22230\python>python now1.py
30
5
Eligable for exam        


#47)Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle. 
side1 = int(input())
side2 = int(input())
side3 = int(input())
if side1==side2 and side1==side3:
    print("Eqvilateral triangle")
elif side1==side2 or side2==side3 or side1==side3:
    print("Issoceless triangle")
else:
    print("Scallen triangle")
    
    
C:\Users\nk22230\python>python now1.py
10
10
20
Issoceless triangle

C:\Users\nk22230\python>python now1.py
10
20
10
Issoceless triangle

C:\Users\nk22230\python>python now1.py
20
10
10
Issoceless triangle

C:\Users\nk22230\python>python now1.py
10
20
30
Scallen triangle

C:\Users\nk22230\python>python now1.py
10
10
10
Eqvilateral triangle