"""
-String Manipulation
-Hashing
-Time complexity: O(n*m)
-Space complexity: O(n*m)
"""

from collections import defaultdict
def fun(strings):
    dic1 = defaultdict(list)
    for i in strings:
        distance = ""
        for j in range(1,len(i)):
            distance += str((ord(i[j]) - ord(i[j-1]))% 26)
        dic1[distance].append(i)
    
    return list(dic1.values())
print(fun(["abc","bcd","acef","xyz","az","ba","a","z"]))