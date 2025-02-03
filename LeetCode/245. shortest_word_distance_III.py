"""
Hash Map / Dictionary
Two-pointer Technique
Time Complexity: O(N+M): 
            N for building the dictionary and
            M for traversing the lists of positions.
Space Complexity: O(N)- N is the number of unique words in the input list due to the space used by the dictionary and lists.
"""

from collections import defaultdict
def fun(wordsDict,word1,word2):
    minDis = float('inf')
    dic1 = defaultdict(list)
    for i in range(len(wordsDict)):
        dic1[wordsDict[i]].append(i)

    if word1 != word2:
        positions1 = dic1[word1]
        positions2 = dic1[word2]
        i,j=0,0
        while i <len(positions1) and j < len(positions2):
            minDis = min(minDis, abs(positions1[i] - positions2[j]))
            if positions1[i] < positions2[j]:
                i += 1
            else:
                j += 1
    else:
        positions1 = dic1[word1]
        for i in range(len(positions1)-1):
            minDis = min(minDis,positions1[i+1] - positions1[i])

    return minDis

print(fun(["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"))