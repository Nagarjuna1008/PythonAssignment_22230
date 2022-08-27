Solve without using builtin methods:
==========================================================

1. WAP to print middle charector of the string 
origional_string = input()
if len(origional_string)>0:
    index = len(origional_string)//2
print("Middle character is ", origional_string[index]) 

#output
helloworld
Middle character is  w

C:\Users\nk22230\python>python Exercise_problems1.py
abc
Middle character is  b   



2. WAP to print half reverse of the string 

Input: KNOWLEDGE
Output: EGDELKNOW

origional_string = input()
if len(origional_string)>0:
    index = len(origional_string)//2
sub_string1 = origional_string[-1:index-1:-1]
sub_string2 = origional_string[:index:1]
half_reverse_string = sub_string1+sub_string2
print(half_reverse_string)

#output
C:\Users\nk22230\python>python Exercise_problems1.py
knowledge
egdelknow

C:\Users\nk22230\python>python Exercise_problems1.py
hello
ollhe


3. WAP to remove all the vouels from the given string 
st="Anil kumar Nahak"
vow="aeioiAEIOU"
for i in st:
    if i not in vow:
        print(i,end="")
#oputput
nl kumr Nhk



4. WAP to insert * in front of every vouels in the string.

Input: BANANA
Output: B*AN*AN*A

st="BANANA"
vow="aeioiAEIOU"
for i in st:
    if i in vow:
        print("*",i,end="")
        continue
    else:
        print(i,end="")

#output
B* AN* AN* A



5. WAP to count number of words in the string.
st="BANANA"
for i in st:
    print(st.count(i),end="")

#output
132323



6. WAP to remove extra space from the given string 
st="Ojas innovative technologies"
for i in st:
    if i==" ":
        continue
    else:
        print(i,end="")

#output
Ojasinnovativetechnologies



7. WAP to insert string in between the given string
Input: Ojas technologies 
Output: Ojas innovative technologies 
In="Ojas technologies"
x=In.index(" ")
print(In[:x]+" innovative"+In[x:])

#output
Ojas innovative technologies



8. WAP to find the ascci value of given char
for i in input("Enter String "):
    print(i," -> ",ord(i))

#output    
Enter String aSH
a  ->  97
S  ->  83
H  ->  72


9. insert ojas in front of every string
a="innovative"
print("ojas"+" "+a)

#output
ojas innovative 



10. insert ojas in every extra space in the string
In=input("enter a string : ")
for i in In:
    if i == " ":
        print(" ojas",i,end="")
        continue
    else:
        print(i,end="")

#output
enter a string : i love my India
i ojas  love ojas  my ojas  India 