def solution(N, number):
    answer = -1
    dp = []
    
    for i in range(1,9):
        case = set()
        num = int(str(N)*i) #지금 숫자
        case.add(num)
        #dp3은 555, dp1연산 dp2, dp2 연산 dp1 
        for j in range(0, i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    case.add(op1 - op2)
                    case.add(op1 + op2)
                    case.add(op1 * op2)
                    if op2 != 0:
                        case.add(op1 // op2)
        if number in case:
            answer = i 
            break
        dp.append(case)
    
    
    return answer
