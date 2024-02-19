thisset={"apple","banana","cherry"}
thisset.add("orange")
print(thisset)
thisset.remove("banana")
print(thisset)


x={"red","green","white"}
y={"blue","yellow","white"}
z=x.intersection(y)
print(z)

a={"apple","orange","watermelom","kiwi"}
b={"cherry","lemon","apple"}
c=a.union(b)
print(c)

a={"apple","orange","watermelom","kiwi"}
b={"cherry","lemon","apple"}
c=a.symmetric_difference(b)
print(c)

myset={"apple","orange","watermelom","kiwi"}
print(len(myset))


myset={8,3,7,1,5}
mylist=list(myset)
maximum=max(mylist)
minimum=min(mylist)
print("maximum",maximum)
print("minimum",minimum)
print(myset)

x={"apple","kiwi","banana"}
y={"orange","coconut","lemon"}
z=x.isdisjoint(y)
print(z)

a={4,7,2,4}
sum=sum(a)
print("sum",sum)






