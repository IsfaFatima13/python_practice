# QNO1:    give greatest of all 4 numbers '
a=int(input("enter 1 number "))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
d=int(input("enter 4th number"))

if(a>b and a>c and a>d):
    print(a," is greater")
elif(b>a and b>c and b>d):
    print(b," is greater")
elif(c>b and c>a and c>d):
    print(c," is greater")
else:
    print (d," is the greater ")
#  QNO2 

# QNO3 print a spam comment 
a="win"
b="cllick"
c="deal"
d="offer"
message=input("enter a message: ")
if((a in message) or (b in message) or (c in message) or (d in message)):
    print("message is spam")
else:
    print("message is not spam")

#QNO4 give if the name is in list 
l=["isfa","izza","fatima","saiqa"]
name=input("enter your name: ")
if(name in l):
    print(name," is in the list ")
else:
    print ("your name is not in list" )
# QNO5 username contain 10 worde 
user=input("enter user name : ")
if(len(user)>=10):
    print("its valid user name ")
else:
    print("enter valid")
# QNO6