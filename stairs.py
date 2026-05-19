#to find the possible combinations to go up 'n' number of stairs


#function to find the possible combinations
def stair(n):
    if n <= 2: #for 0,1,2 values of n, the possible combinations is n itself
        return n
    dp = [0] * (n+1)    #initilize dp with n number of blank spaces
    
    #to find using the fibonacci series
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):  #from the third index till the last index
        dp[i] = dp[i-1] + dp[i-2]   #new value = sum of previous 2 values
    return dp[n]

m = int(input("Enter the number: "))

result = stair(m)
print(result)