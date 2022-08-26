Loops
============================================================================================

#1)Accept 10 numbers from the user and display their average. 
number = int(input())
sums = 0
for i in range(number):
    num = int(input())
    sums+=num
average = sums/number  
print(average)

#output
10
1
2
3
4
5
6
7
8
9
10
5.5  




#2)Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)
sum_even = 0
sum_odd = 0

for i in range(12,38):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
        
print(sum_even, sum_odd)        

#output
312 325




#3)Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500. 
for i in range(100,500):
    if i%11==0 and i%2!=0:
        print(i, end=" ")
        
C:\Users\nk22230\python>python now1.py
121 143 165 187 209 231 253 275 297 319 341 363 385 407 429 451 473 495 




#4)Write a program to print numbers from 1 to 20 except multiple of 2 & 3  
for i in range(1,21):
    if i%2!=0 and i%3!=0:
        print(i, end=" ")
        
#output
1 5 7 11 13 17 19        
        



#5)Write a program that keep on accepting number from the user until user enters Zero. Display the sum and average of all the numbers
sums = 0
count = 0
while True:
    number = int(input())
    if number==0:
        break
    else:
        count+=1
        sums+=number
print("sum of numbers = ",sums, "\nAverage of numbers = ", sums/count)        

#output
10
20
30
40
50
0
sum of numbers =  150
Average of numbers =  30.0



#6)Write a program to accept decimal number and display its binary number.
num = float(input()) 
def binary_number(num):
    ls=[]
    while num>0:
        rem=num%2
        ls.append(rem)
        num=num//2
    #print(ls)
    return ls 
    
 
list1 = binary_number(num)
for i in list1:
    print(int(i),end="")

#output
5
101
    





#7)Convert the following loop into for loop : 

x = 4 

while(x<=8): 

    print(x*10) 

    x+=2 

for i in range(4,9,2):
    print(i*10)    
    
40
60
80     




#8)What is nested loop? 
A nested loop is a loop inside the body of the outer loop. 
The inner or outer loop can be any type, such as a while loop or for loop.
For example, the outer for loop can contain a while loop and vice versa.


#9)Write a program to convert temperature in Fahrenheit to Celsius
temperature = float(input())
print("fahrenheit in celcius is", (temperature-32)*5/9)

#output
100
fahrenheit in celcius is 37.77777777777778



#10)Write a Python program to get the Fibonacci series between 0 to 50.  
num = int(input())
first_number = 0
second_number = 1
print(first_number, second_number, end=' ')
for i in range(1,num+1):
    third_number = first_number+second_number
    if third_number<=50:
        print(third_number, end=" ")
    first_number, second_number = second_number, third_number    
    
#output
50
0 1 1 2 3 5 8 13 21 34    




#11)Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz". 

Sample Output : 

fizzbuzz 

1 

2 

fizz 

4 

Buzz 

num = int(input())
for i in range(num+1):
    if i%3==0 and i%5==0:
        print("FizzBuss")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        
#output
50
FizzBuss
1
2
fizz
4
Buzz
fizz
7
8
fizz
Buzz
11
fizz
13
14
FizzBuss
16
17
fizz
19
Buzz
fizz
22
23
fizz
Buzz
26
fizz
28
29
FizzBuss
31
32
fizz
34
Buzz
fizz
37
38
fizz
Buzz
41
fizz
43
44
FizzBuss
46
47
fizz
49
Buzz 





       
#12)Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
num = int(input())
for i in range(num+1):
    if i==3 or i==6:
        continue
    print(i, end=" ")

#output
6
0 1 2 4 5