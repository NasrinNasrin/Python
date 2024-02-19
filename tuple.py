fruits=list(("cherry","orange","kiwi"))
(red,yellow,green)=fruits

print(red)
print(yellow)
print(green)

thistuple=("apple","banana","cherryy")
y=list(thistuple)
y.append("orange")
#thistuple=tuple(y)
#print(thistuple)

#thistuple=("apple","banana","cherry","mango","kiwi","melon","mango","orange")
#print(thistuple[4:])


l=[(10,20,40),(40,50,60),(70,80,90)]
print([t[:-1]+(100,)for t in l])


L= [(),(),('',),('a','b'),('a','b','c'),('d')] 
L=[t for t in L if t]
print(L)







