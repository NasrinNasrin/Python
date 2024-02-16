a=int(input("enter project score"))
b=int(input("enter exam score"))
sum1=a+b
print("sum",sum1)
if sum1>60:
     print("grade A")
elif sum1<50 and sum1>50:
    print("grade B")
elif sum1<=40:
    print("grade C")
else: 
    print("grade D")

x=a//5
for i in range(x):
    print("=",end="")
print()
y=b//5
for i in range(y):
    print("=",end="")
print()
z=sum1//5
for i in range (sum1+1):
    print("=",end="")


    



