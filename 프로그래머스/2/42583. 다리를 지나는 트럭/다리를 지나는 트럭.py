# 다리를 지나는 트럭 

from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 길이만큼 큐에 0을 둠 길이 4면 [0,0,0,0]
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    
    # 현재 시간, 현재 다리 위 무게 
    time = 0
    current_weight = 0
    

    # 다리나 대기하고 있는 트럭 있으면 Loop
    while truck_weights or current_weight > 0:
        time += 1
        
        # 다리 한칸 앞으로 이동 
        current_weight -= bridge.popleft()
        
         # 현재 다리 무게 + 다음 트럭이 최대 무게 이하이면 
        if truck_weights and current_weight + truck_weights[0] <= weight:
            # 대기 리스트에서 하나 뺌 
            truck = truck_weights.popleft()
            # 트럭 올림 
            bridge.append(truck)
            current_weight += truck
        else:
            # 못올리면 그냥 빈칸 추가 
            bridge.append(0)
    
                
                
    return time 