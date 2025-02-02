"""
Technique: Two-Pointer Technique combined with In-place Reversal.
Time Complexity: O(n).
Space Complexity: O(1).
"""

def fun(s):
    start,end= 0 ,len(s) -1
    while start < end:
        s[start], s[end] = s[end],s[start]
        start +=1
        end -=1
    j,k = 0,0
    for i in range(len(s)):
        if s[i] == " " or i == len(s) - 1:
            if i == len(s) - 1:
                k = i
            else:
                k = i - 1
            while j < k:
                s[j], s[k] = s[k], s[j]
                j += 1
                k -= 1
            j = i + 1
    return s
print(fun(["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
))