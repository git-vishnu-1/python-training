def rob(nums):
    #if the array / list is empty or has only on element
    if not nums:
        return 0
    if len(nums) == 1:
        return (nums[0])
    #if the array / lists has 2 or more elements
    def houses(arr):
        prev = 0    #previous = 0
        curr = 0    #current = 0
        for n in arr:   #iterate throughout the array and check the following
            new = max(curr, prev + n)   #put the max of current value and the (previous + n(index value)) in new
            prev = curr #put current value as previous
            curr = new  #put the new value as current value (to shift to the right, and select the next element)
        return (curr) #return statement of the inside function which returns the current value, i.e, the max value of things stolen from houses
    return max(houses(nums[:-1]), houses(nums[1:])) #return statement of the main function which returns the two values of the cases and checks which one is the max

nums = [2,7,9,3,1]  #the array we check
print(rob(nums))    #result printing