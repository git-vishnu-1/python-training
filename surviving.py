n = int(input("Enter the number: "))
x = 0
while 2**x <= n:
    x+=1
x = x - 1
survivor = 1  + (n - x) * 2
print(survivor)