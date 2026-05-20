#given 2 arrays gas and cost. gas[] shows how much gas a gas station provides. cost[] shows the cost of petrol to go from one station to the next one
#find the starting index so that a full trip can be completed

def circuit(gas,cost):  #function to find the starting index where a full trip can be completed
    
    #if the overall sum of gas list is less than the overall sum of cost then return -1
    if sum(gas) < sum(cost):
        return -1
    
    start_index = 0 #for we don't know the starting index
    current_tank = 0    #gas in the tank

    for i in range(len(gas)):   #iterates through the array / list

        #checks if the difference is -ve or +ve
        current_tank += gas[i] - cost[i]
        
        #if -ve then shift to next index and put current tank = 0
        if current_tank < 0:    
            start_index = i + 1
            current_tank = 0
    
    #if the iteration is complete then return the last start index
    return start_index

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(circuit(gas,cost))