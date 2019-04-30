def findLimit(M,x, budgets):
    B = 0
    n = 1
    if (M-(B+x*n))//n>=1:
        for i in 


def solution(budgets, M):
    dLine = findLimit(M, (sum(budgets)/len(budgets)),budgets)
        
    return dLine

print(solution([225,280,300,250],1000))