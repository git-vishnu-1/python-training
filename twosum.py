#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def twosum(nums,target):
    if not nums: print(0)
    else:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(i,j)
                    break

nums = [2,7,11,15]
target = 9

twosum(nums, target)

#better way with one 'for loop'

def twosumbetter(nums,target):
    seen = {}
    for i,num in enumerate(nums):
        compliment = target - num
        if compliment in seen:
            return(seen[compliment],i)
        seen[num] = i
    return []

twosumbetter(nums,target)