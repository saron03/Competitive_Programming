"""
Two-pointer technique 
Time Complexity: O(n)
Space Complexity: O(1)
"""

def fun(s,t):
    n,m = len(s), len(t)
    if n > m:
        s,t = t,s
        n,m = m,n
    if m - n > 1 or s == t:
        return False
    count = 0
    i,j = 0, 0
    while i < n and j < m:
        if s[i] != t[j]:
            count +=1
            if n == m:  
                i += 1
            j+=1
        else:
            i+=1
            j+=1
        if count > 1:
            return False
    return True