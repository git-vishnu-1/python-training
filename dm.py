# to find the duplicate and missing numbers in the array

#array
nums=[3,1,2,5,3]

#length of the array
n=len(nums)

exp_sum = (n*(n+1))//2
act_sum = sum(nums)

exp_sq_sum = (n*(n+1)*(2*n+1))//6
act_sq_sum = sum(x*x for x in nums)

#differences
temp = act_sum - exp_sum
tempsq = act_sq_sum - exp_sq_sum

#d2 - m2 divided by d - m = d + m
sum_linear = tempsq // temp

#to find duplicate
duplicate = (temp + sum_linear) // 2

#to find missing
missing = sum_linear - duplicate

print(duplicate)
print(missing)