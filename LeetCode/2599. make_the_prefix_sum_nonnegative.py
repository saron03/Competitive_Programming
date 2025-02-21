"""
-Greedy approach
-prefix sum
-Time complexity: O(n)
-Space complexity: O(1)
"""

def fun(nums):
    count = 0
    for i in range(1,len(nums)):
        if nums[i-1] + nums[i] < 0:
            nums[i],nums[-1] = nums[-1],nums[i]
            count +=1
        nums[i] = nums[i-1] + nums[i]
    return count

print(fun([2,3,-5,4]))
    