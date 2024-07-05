def solution(order):
    answer = 0
    belt = []
    idx = 0 
    
    for box in range(1, len(order)+1):
        belt.append(box)
        
        #belt가 비어있지 않고, 맨 위가 현재의 순서와 같을 때
        while (belt) and (belt[-1] == order[idx]):
            answer += 1
            idx += 1
            belt.pop()
            
    return answer   