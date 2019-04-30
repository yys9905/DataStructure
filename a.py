def findLimit(x):
    

def solution(budgets, M):
    temp = 0
    count = 0
    a = 0
    dLine = int(M / len(budgets))
    for i in budgets:
        if i <= dLine:
            temp += dLine - i
            a += i
        else:
            count += 1
    if count == 0:
        return 0
    
    if temp != 0:
        dLine += int(temp / count)
    a = M - (dLine * count + a)
    while(True):
        if a >= count:
            dLine += int(a/count)
            a = M - (dLine * count + a)

        if int(a/count) == 0:
            break
        
    return dLine

print(solution([225,280,300,250],1000))