#to find the max number of a's in a window using sliding window protocol

str = str(input("Enter a string: "))    #actual string
n = int(input("Enter the number of times to repeat the string: "))  #window-size

#to find the number of a's in the first window manually
count = str[:n].count('a')
max_a = count


#for the rest windows
for i in range(1,len(str) - n):
    count -= 1 if str[i-1] == 'a' else 0    #the previous element was 'a'
    count += 1 if str[i+n-1] == 'a' else 0  #the next element is 'a'
    max_a = max(max_a, count)   #to find if the first one that we done manually had the max number or the current one that we just did had the max number of a's

print("Maximum number of 'a' in any substring of length", n, "is:", max_a)