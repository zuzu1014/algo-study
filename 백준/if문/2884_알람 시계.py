H, M = input().split()
H = int(H)
M = int(M)

M = M -45

if M >= 0:
    print(H,M)
else:
    M = 60 + M
    H = H-1
    if H >= 0:
        print(H,M)
    else:
        H = 23
        print(H, M)