#to shift all the zeroes in a list to the right most side

arr=[0,0,5,0,45,2,4,0,6,0,1,0,0,4]
br=[]
jr=[]
for i in arr:
    if i==0:
        br.append(i)
    else:
        jr.append(i)
arr=br+jr
print(arr)
