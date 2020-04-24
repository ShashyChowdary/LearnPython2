num = int(input("Enter a Number : "))

if num > 1 :
   for i in range(2, num) :
       # print('printiteration number ', i)
       r = num % i
       # r='shashy'
       if i == 10 :
           continue
       print('i am not 10', i)
       if (r == 0) :
            print('num' "is not a prime number")
             # print (i,"times",num//i,"is",num)
            break
       else :
            print(num,"is a prime number")

else  :
    print(num,"is not a prime number")


