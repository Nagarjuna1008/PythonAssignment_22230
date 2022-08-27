1. How would you confirm that 2 strings have the same identity?
The is operator returns True if 2 names point to the same location in memory
num1 = 'arjun'
num2 = 'arjun'
if id(num1)==id(num2):
    print("same identity")
else:
    print("No")
    
#output
C:\Users\nk22230\python>python Exercise_problems1.py
same identity 




2. How would you check if each word in a string begins with a capital letter?
org_str = input().split()
for i in org_str:
    if i[0].isupper():
        print("True")
    else:
        print("False")
        
#output
C:\Users\nk22230\python>python Exercise_problems1.py
h
False

C:\Users\nk22230\python>python Exercise_problems1.py
hello How are You
False
True
False
True       




3. Check if a string contains a specific substrin
full_string = input()
sub_string = input() 
if sub_string in full_string:
    print("True")
else:
    print("False")  

#output
C:\Users\nk22230\python>python Exercise_problems1.py
hello how Are you
you
True

C:\Users\nk22230\python>python Exercise_problems1.py
hello how Are you
hai
False    



4. Find the index of the first occurrence of a substring in a string
full_string = input()
sub_string = input() 
if sub_string in full_string:
    print(full_string.index(sub_string))
else:
    print("False")

#output    
C:\Users\nk22230\python>python Exercise_problems1.py
hello world hello
hello
0   

5. Count the total number of characters in a string
org_str = input()
count=0
for i in org_str:
    if i==' ':
        continue
    count+=1
print(count)   

#output    
C:\Users\nk22230\python>python Exercise_problems1.py
hello
5

C:\Users\nk22230\python>python Exercise_problems1.py
hello world
10    



6. Count the number of a specific character in a string
org_str = input()
#print(org_str.count(input()))

count=0
j=input()
for i in org_str:
    if j in i:
        count+=1
print(count) 

#output
C:\Users\nk22230\python>python Exercise_problems1.py
hello
l
2

C:\Users\nk22230\python>python Exercise_problems1.py
hello world how are you
o
4     




7. Capitalize the first character of a string
 character_string = ''


org_string = input()
print(org_string.capitalize())
#output
anil
Anil 





8. What is an f-string and how do you use it?
f-string is a formating string

In Python source code, an f-string is a literal string, prefixed with f , 
which contains expressions inside braces. The expressions are replaced with their values
Using f-strings is similar to using format().
F-strings are denoted by an f before the opening quote.
a = 10
b = 20
c = 30
print(f'{a} and {b} sums is {c}')  

#output
10 and 20 sums is 30




#9. Search a specific part of a string for a substring
s1 = input()
s2 = input()
print(s1.index(s2))
#output
hello world, how are you
l
2  

 
10. Interpolate a variable into a string using format()
boy = 'Nagarjuna'
charec = 'good'
print('this {} is very {}'.format(boy,charec))
#output
C:\Users\nk22230\python>python Exercise_problems1.py
this Nagarjuna is very good


#11. Check if a string contains only numbers
s1 = input()
print(s1.isnumeric()) 

#output
C:\Users\nk22230\python>python Exercise_problems1.py
hello123
False

C:\Users\nk22230\python>python Exercise_problems1.py
1234566
True




12. Split a string on a specific character
s1 = input()
char = input()
print(s1.split(char))

#output
hello world
l
['he', '', 'o wor', 'd']

C:\Users\nk22230\python>python Exercise_problems1.py
nagarjuna
a
['n', 'g', 'rjun', '']



13. Check if a string is composed of all lower case characters
s1 = input()
print(s1.islower())

#output
hai how
True

C:\Users\nk22230\python>python Exercise_problems1.py
Hai how
False



14. Check if the first character in a string is lowercase
s1 = input()
print(s1[0].islower())

#output
hello world
True

C:\Users\nk22230\python>python Exercise_problems1.py
Hello
False



15. Can an integer be added to a string in Python?
NO string and int can not be added
s1 = 'hello'
s2 = 2
print(s1+s2)




16. Reverse the string “hello world”
s1 = 'hello world'
print(s1[-1::-1])

#output
dlrow olleh



17. Join a list of strings into a single string, delimited by hyphens
s1 = input()
s2 = input()
s3= s1.join(s2)
print(s3)

#output
hello
world
whelloohellorhellolhellod

C:\Users\nk22230\python>python Exercise_problems1.py
-
abc
a-b-c



18. Check if all characters in a string conform to ASCI
print('A'.isascii())
True


19. Uppercase or lowercase an entire string
s1 = input()
print(s1.upper())
print(s1.lower())

hello World
HELLO WORLD
hello world



20. Uppercase first and last character of a string
s1 = input()
print(s1[0].upper()+s1[1:len(s1)-1:1].lower()+s1[-1::].upper())

#output
prem
PreM




21. Check if a string is all uppercase
string=input("enter a string : ")
print(string.isupper())

#output
enter a string : ANIL KUMAR
True





22. When would you use splitlines()?
The splitlines() method splits a string into a list.
 The splitting is done at line breaks. 




23. Give an example of string slicing
s1 = 'Hello world'
print(s1[0:11:2])

#output
Hello world



24. Convert an integer to a string
inpt=int(input("enter an integer: "))
print(type(inpt))
st=str(inpt)
print(type(st))

#output
enter an integer: 25
<class 'int'>
<class 'str'>


25. Check if a string contains only characters of the alphabet
inpt=input("enter a string : ")
print(inpt.isalpha())

#output
enter a string : naga
True



26. Replace all instances of a substring in a string
string_a = "Hello Anil Kumar"
string_b = string_a.replace("Anil","Rakesh")
print(string_a)
print(string_b)

#output
Hello Anil Kumar
Hello Rakesh Kumar'''



27. Return the minimum character in a string
st=input("enter a string : ")
for i in st:
    st.count(i)
print(min(i))

#output
enter a string : aaabbbc




28. Check if all characters in a string are alphanumeric
string="anil1234"
print(string.isalnum())

#output
True




29. Remove whitespace from the left, right or both sides of a string
st="     welcome    "
print(st.strip())

#output
welcome

30. Check if a string begins with or ends with a specific character?
st="Anil kumar"
print(st.startswith("A"),st.endswith("a"))

#output
True False