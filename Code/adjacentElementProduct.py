
l=[2,4,1,6,8,1,3,9,2]
m=zip(l[:-1],l[1:])
k=0
for i in m :
    p=i[0]*i[1]
    if p>k :
        k=p
print (k)

print("shashy")








