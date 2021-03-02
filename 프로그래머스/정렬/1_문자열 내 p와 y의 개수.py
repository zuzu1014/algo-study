def solution(s):
    num_p = 0
    num_y = 0
    
    s = s.lower()
    
    num_p = s.count('p')
    num_y = s.count('y')
    
    if num_p == num_y:
        return True
    else:
        return False