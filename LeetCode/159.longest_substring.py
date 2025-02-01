""""
Sliding Window Technique
HashMap for Frequency Tracking
Time Complexity: O(n)
Space Complexity: O(1)
"""

def fun(s):
    count = {}
    j=0
    maxLen=0
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] +=1
        else:
             count[s[i]] = 1
           
        while len(count) > 2:
            if count[s[j]] == 1:
                del count[s[j]]
            else:
                count[s[j]] -=1
            j +=1
        maxLen = max(maxLen, i - j + 1)
    return maxLen
