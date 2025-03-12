def fun(nums):
    j=1
    product =1
    count = 0
    for i in range(len(nums)):
        if product % 2 == 0:
            count +=1 
        product *= nums[i]
        if i == len(nums) -1:
            while j < len(nums):
                if nums[j] % 2 ==0:
                    count +=1
                j+=1
    return count 
print(fun([9,6,7,13]))