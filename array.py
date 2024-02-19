#a="hi,this is python"


#b="hellooo.python"
#print(b.split("."))
#c="hy"
#d="python"
#print(c+""+d)

#age=21
#name="anu"
#count=3.9
#txt="my age is {},name is {},{} is my count"
#print(txt.format(age,name,count))

#a="python is highlevel language"
#print(a.upper())
#print(a.capitalize())
#print(a.count("l"))
#print(a.center(70))
#print(a.endswith(""))
#print(a.find("e"))


mytuple=('apple','orange','mango')
x="*".join(mytuple)
print(x)
y=('apple','orange','mango')
z=(mytuple)
print(mytuple is y)
print(y is not z)
print("mango" in z)
print("lemon"not in y)


a=20
b=50
c=10
if(a<b) and (a>c): print("a is lowest number")
        
elif(b>c) and (b>=50):
    print("b is lowest no")
else:
  print("b is highest no")


#a=20
#b=10
#if(a>b) and (a<18):
  # print("a is highest no " and "a is minor")
#elif(a==b):
  #  print("a and b are same")   
#else:
   print("b is lowest no")

#a=30
#b=20
#print("a is highest no")if a > b else print("b is highest no")

i=0
while  i<6:
  i += 1
  if(i==3):
    continue
print(i)
    




    






