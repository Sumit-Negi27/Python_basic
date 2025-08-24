a=int(input("enter any no."))
if(a%2==0):
    print("it is a even no.")
else:
    print("odd no.")

b=int(input("enter any no."))
c=int(input("enter any no."))
d=int(input("enter any no."))
if(d>b and d>c):
    print("the greatest no. is= ",d)
elif(b>c and b>d):
    print("the greatest no. is= ",b)
else:
    print("greatest no. is=",c)