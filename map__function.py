a=input('enter input')
b=[]
c=a.split()

for i in c:

    if(i.isdigit()):
        d=int(i)
        b.append(d)

print(b)

l1=list(map(lambda x:int(x),a.split()))  #in single line
print(l1)
