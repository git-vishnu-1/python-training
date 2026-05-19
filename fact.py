def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

m = int(input("Enter number: "))
result = fact(m)
print(result)