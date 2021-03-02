def converter(n, base):
    result = ''
    while n:
        q,r = divmod(n,base)
        result = str(r) + result
        n = q
    
    print(result)
    
converter(10,3)