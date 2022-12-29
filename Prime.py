a=int(input("enter a first no.\n"))
b=int(input("ener last no.\n"))
c1=0
c2=0
for i in range(a,b+1):
    for j in range(2,i):
        if(i%j==0):
            print(i,"is composite")
            c1+=1
            break
    else:
        print(i,"is a prime no.")
        c2+=1
print(c2,"prime and",c1,"composite numbers in the range.")   