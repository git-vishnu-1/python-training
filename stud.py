
n = int(input("Enter the number of students: "))
a = 0
b = 1

for i in range(1,n+1):
    c = (a+b)*(i-1)
    a = b
    b = c
print("Possible combinations: ", end="")
print(c)