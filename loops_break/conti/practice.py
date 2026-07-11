# #QNO1 print table
# a=int(input("enter a number to calculate table: "))

# for i in range(1,11):
#     print(f"{a}*{i} ={a*i}")
# i=0#through while loop
# while(i<11):
#     print(f"{a}*{i}={a*i}")
#     i+=1
# #QNO2 print name with i 
# list=["isfa","fatima","izza","iqra","rimsha"]
# for i in range(len(list)):
#     if(list[i].startswith("i")):
#         print(list[i])
# print("these are names")

# list=["isfa","fatima","izza","iqra","rimsha"]
# for i in list:
#     if(i.startswith("i")):
#         print(i)
#         print("names\n")
        

# print(list)6
# #QNO3 prime number 
# a=int(input("enter a number: "))
# for i in range(2,a):
#     if((a%i/2)==0):
#         print(a,"number is not prime")
#         break
# else:
#     print ("number is prime")
# print("checked")
# #QUNO4 sum numbers upto n 
# n=int(input("Enter number to sum: "))
# i=0
# sum=0
# while(i<=n):
#     sum=sum+i
#     i+=1
# print(sum)
# #QNO5 find factorial
# x=int(input("Enter number to factorial: "))
# result=1
# if(x==0):
#     print(result)
# for i in range(1,x+1):
#     result=result*i
# print(result)
# #QNO6 print star pattren 
# '''  *
#     ***
#    ***** '''
# n=int(input("enter a number: "))
# for i in range (1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1))
# #QNO7 * ** ***
# n=int(input("enter a number : "))
# for i in range (1,n+1):
#     print("*"*(i))
''' ***
    * *
    ***'''
n=int(input("enter a number: "))
for i in range (1,n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")