#to find the last surving element in n elements. If 1 has the knife, 1 kills 2 and passes the knife to 3. Like wise till only 1 element is left.
#HINT : write the n elements in a circle and eliminate using the above rule for n elements, then find the pattern and form an equation

n = int(input("Enter the number: "))
x = 0
while 2**x <= n:
    x+=1
x = x - 1
survivor = 1  + (n - x) * 2
print(survivor)