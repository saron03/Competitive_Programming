"""
Two-Pointer Technique
HashMap
Time Complexity: O(n)
Space COmplexity:  O(1)
"""

def is_strobogrammatic(num):
    nums = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in nums or nums[num[left]] != num[right]:
            return False
        left += 1
        right -= 1

    return True