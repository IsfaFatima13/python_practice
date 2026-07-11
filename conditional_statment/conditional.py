a= int(input("enter your age: "))
if(a%2==0):
    print("number is even ")
if(a<0):
    print("enter a valid age ")
elif(a>=50):
    print("you are old...!\n donot enter the game ")
    a=a+2
    print(a)

else:
    print("you are not old\n you can enter the game ")
    a=a+3
    print(a)

print(a)