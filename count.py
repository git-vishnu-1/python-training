str = str(input("Enter a string: "))
n = int(input("Enter the number of times to repeat the string: "))

count = str[:n].count('a')
max_a = count

for i in range(1,len(str) - n):
    count -= 1 if str[i-1] == 'a' else 0
    count += 1 if str[i+n-1] == 'a' else 0
    max_a = max(max_a, count)

print("Maximum number of 'a' in any substring of length", n, "is:", max_a)