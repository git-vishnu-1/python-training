#to find the max number of cakes that an employee can take home by considering how many cakes per packet and should have enough cake to fill the whole packet.
#example : if there are 5 cakes and each packet contains 2 cakes, then there is only 1 cake in the last packet. this is not possible, so the employee can take the cake.

c=int(input("enter the number pf cakes: "))
if c%2==0:
    h=(c/2)+1
    print(c-h)
else:
    h=c//2
    print(h)
