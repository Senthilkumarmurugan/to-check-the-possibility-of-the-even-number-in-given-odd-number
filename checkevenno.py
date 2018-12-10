a="56321"
l=list(a)
l[1],l[4]=l[4],l[1]
s="".join(l)
print(s)
x=list(a)
x[3],x[4]=x[4],x[3]
t="".join(x)
print(t)

if (s>t):
    print("s is a greater number"+s)
else:
    print("t is greater:"+t)
    
