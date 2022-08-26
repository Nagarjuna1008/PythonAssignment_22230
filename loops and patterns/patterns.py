Patterns
=========================================================================================== 
1. Write a program to print the following Patterns

  1 2 3 4 5 
  1 2 3 4 5  
  1 2 3 4 5 
  1 2 3 4 5 
  1 2 3 4 5


number=int(input("Enter the number"))
for rows in range(1,number+1):
    for columns in range(1,number+1):
        print(columns," ",end="")
    print("")

2.Write a program to print the following Pattern

  5 4 3 2 1 
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1 



number=int(input("Enter the number"))
for rows in range(number,0,-1):
    for columns in range(number,0,-1):
        print(columns," ",end="")
    print("")

3.Write a program to print the following Pattern
  5 5 5 5 5 
  4 4 4 4 4 
  3 3 3 3 3 
  2 2 2 2 2 
  1 1 1 1 1


number=int(input("Enter the number"))
temp=number
for rows in range(number,0,-1):
    for columns in range(number,0,-1):
        print(temp ," ",end="")
    temp=temp-1
    print("")

4. Write a program to print the following Pattern
  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5



number=int(input("Enter the number"))
for rows in range(1,number+1):
    for columns in range(1,rows+1):
        print(columns ," ",end="")
    print("")

5.Write a program to print the following Pattern
  1 
  2 2 
  3 3 3 
  4 4 4 4 
  5 5 5 5 5



number=int(input("Enter the number"))
for rows in range(1,number+1):
    for columns in range(0,rows):
        print(rows ," ",end="")
    print("")

6.Write a program to print the following Pattern
  1 
  2 3  
  4 5 6 
  7 8 9 10 
  11 12 13 14 15



number=int(input("Enter the number"))
temp=1
for rows in range(1,number+1):
    for columns in range(0,rows):
        print(temp ," ",end="")
        temp+=1
    print("")

7.Write a program to print the following Pattern
  5 
  4 4 
  3 3 3 
  2 2 2 2 
  1 1 1 1 1


number=int(input("Enter the number"))
temp=number
for rows in range(0,number):
    for columns in range(0,rows+1):
        print(temp ," ",end="")
    temp-=1
    print("")

8.Write a program to print the following Pattern
  1 
  2 3 
  3 4 5 
  4 5 6 7 
  5 6 7 8 9



number=int(input("Enter the number"))
for rows in range(1,number+1):
    temp=rows
    for columns in range(0,rows):
        print(temp ," ",end="")
        temp+=1
    print("")

9.Write a program to print the following Pattern
  A 
  B C
  D E F
  G H I J
  K L M N O


number=int(input("Enter the number"))
temp=65
for rows in range(1,number+1):
    for columns in range(0,rows):
        print(chr(temp)," ",end="")
        temp+=1
    print("")

10.Write a program to print the following Pattern
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 


number=int(input("Enter the number"))
for rows in range(number,0,-1):
    for columns in range(number,0,-1):
        print("*"," ",end="")
    print("")

11.Write a program to print the following Pattern
   * 
   * * 
   * * * 
   * * * * 
   * * * * * 


number=int(input("Enter the number"))
for rows in range(1,number+1):
    for columns in range(1,rows+1):
        print("*" ," ",end="")
    print("")

12.Write a program to print the following Pattern
    * * * * * 
    *       * 
    *       * 
    *       * 
    * * * * * 


number=int(input("Enter the number"))
for rows in range(1,number+1):
    for columns in range(1,number+1):
        if rows == 1 or rows == number:
            print("*"," ",end="")
        elif columns ==1 or columns == number:
             print("*"," ",end="")
        else:
            print("  ",end=" ")
    print("")



13.Write a program to print the following Pattern
          * 
        * * * 
      * * * * * 
    * * * * * * *
number=int(input("Enter the number"))
k = 0
for i in range(1, number+1):
    for space in range(1, (number-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()

14.Display Multiplication Table in given range using Nested for loop


for rows in range(1,11):
       for columns in range(1,11):
           print(rows*columns," ",end="")
       print("")




15.Display Prime Numbers in the given range using nested for loops 

print("List of prime numbers from 1 to 100 :")
for n in range (1, 101):
    count = 0
    t = n//2
    for i in range(2, (t + 1)):
        if(n % i == 0):
            count = count + 1
            break
    if (count == 0 and n > 1):
        print(" %d" %n, end = '  ')
        
        
        

16.Write a program to print the following Pattern
                 1
              3  2
          6   5  4
      10  9   8  7
m = int(input())
n = int(input())
k = m
for i in range(1, n+1):
    for j in range(1, (n - i)+1):
        print(" ", end = " ")
    for j in range(1, i+1):
        print(k, end = " ")
        k +=1
    print()




17.Write a program to print the following Pattern
10  9  8   7
      6   5  4
           3  2
               1

t=10
s=0
for i in range(4,0,-1):
    print(' '*s*2,end=' ')
    for j in range(1,i+1):
        print(t,end=' ')
        t-=1
    s=s+1
    print()