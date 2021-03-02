def solution(array, commands):
    

    answer = []
    for c in commands:
        command_array = array[c[0]-1:c[1]]
        command_array.sort()
        answer.append(command_array[c[2]-1])
        
    return answer