"""
Missing Range Detection
Time Complexity: O((n)
Space Complexity: O(1)
"""
def fun(nums,lower,upper):
    res = [] 
    if not nums:
        return [[lower, upper]]
    if nums[0] > lower:
        res.append([lower, nums[0] - 1])

    for i in range(len(nums) -1):
        if nums[i+1] > nums [i] + 1:
            res.append([nums [i] + 1,nums[i+1] -1])

    if nums[-1] < upper:
        res.append([nums[-1] +1, upper])
    return res
print(fun([0, 1, 3, 50, 75], 0, 99))