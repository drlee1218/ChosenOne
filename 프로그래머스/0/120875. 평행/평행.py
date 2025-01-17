def solution(dots):
    a, b, c, d = dots
    if abs((a[0]-b[0]) / (a[1]-b[1])) == abs((c[0]-d[0]) / (c[1]-d[1])) :
        return 1
    elif abs((a[0]-c[0]) / (a[1]-c[1])) == abs((b[0]-d[0]) / (b[1]-d[1])) :
        return 1
    elif abs((a[0]-d[0]) / (a[1]-d[1])) == abs((c[0]-b[0]) / (c[1]-b[1])) :
        return 1
    else :
        return 0