#to find the given factorial using a fucntion


#function to find the factorial
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


#inputs and function calls
m = int(input("Enter number: "))
result = fact(m)
print(result)