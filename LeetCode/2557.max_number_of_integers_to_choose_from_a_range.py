def fun(banned,n,maxSum):
    maxNums = 0
    curSum = 0
    banned = set(banned)
    for i in range(1,n+1):
        if i not in banned:
            if curSum + i < maxSum:
                curSum +=i
                maxNums += 1
            else:
                continue
        else:
            continue
    return maxNums
print(fun([4,3,5,6],7,18))


