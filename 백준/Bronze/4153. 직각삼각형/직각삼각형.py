while(1):
    l=list(map(int, input().split()))
    l.sort()
    if l[0]==0 and l[1]==0 and l[2]==0:
        break
    elif l[2]**2==l[1]**2+l[0]**2:
        print("right")
    else:
        print("wrong")
        
    