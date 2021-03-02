def solution(participant, completion):
    participant.sort()
    completion.sort()
    for index, person in enumerate(completion):
        if (person != participant[index]):
            return participant[index]
        
    return participant[-1]