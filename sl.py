a = [12,35,1,10,34,35]

largest = 0
s_largest = 0

for i in a:
    if i > largest:
        s_largest = largest
        largest = i
    elif i > s_largest and i < largest:
        s_largest = i

print(s_largest)