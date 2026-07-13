import random 
def computerr():
    computer=random.choice([1,0,-1])
    #print(f"{computer} is the choice of computer")
    return computer
you=input("enter your choice (w,g,s): ")
dict={
    "w":-1,
    "s":0,
    "g":1
}
revdict={
    1:"g",
    0:"s",
    -1:"w"
}
yo=revdict[dict[you]]
yourch=dict[you]
print(f"{yo} is your choice")
#print(yourch)
computer=computerr()
co=revdict[computer]
print(f"{co}  is choice of comp")

if(computer==yourch):
    print("its a draw!")
else:
    if(computer==1 and yourch==0):
        print("you lose!")
    elif(computer==0 and yourch==1):
        print("you win!")
    elif(computer==-1 and yourch==1):
        print("you lose!")
    elif(computer==-1 and yourch==0):
        print("you win!")
    elif(computer==0 and yourch==-1):
        print("you win!")
    elif(computer==1 and yourch==-1):
        print("you win!")