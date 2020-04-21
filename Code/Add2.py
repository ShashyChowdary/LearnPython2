# Taking Multiple Inputs and add
m = int(input("How Many Numbers U Want : "))
#list len(5)
s=0
for i in range(m):
    s += int(input("ënter number for {pos} position : ".format(pos=i)))
    # if i<=m :
    #      l1 = int(input("Enter a number : "))
    # else :
    #     for i in range(m) :
print("final sum ", s )