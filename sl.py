#to find the second largest number in an array

a = [12,35,1,10,34,35]

largest = 0
s_largest = 0

for i in a:
    if i > largest: #if the current number is larger than the value in 'largest'
        s_largest = largest #put the largest number as second largest
        largest = i #put the current number as largest
    elif i > s_largest and i < largest: #else if the current number is larger than 'second largest' but smaller than 'largest'
        s_largest = i   #put the current number as second largest

print(s_largest)