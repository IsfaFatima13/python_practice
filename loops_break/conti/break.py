for i in range (100):#skip next part
    if(i==39):
        break
    print(i)

list=[1,3,4,5,"isfa"]
for i in range(len(list)):
    if(i==2):
        continue
    print(i,list[i])

for i in range(100):#pass statment 
    pass
i=0
while(i<6):
    print(i,"is number")
    i+=1