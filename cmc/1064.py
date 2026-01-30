xa, ya, xb, yb, xc, yc = map(int, input().split())

def dist(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# 세점이 직선이면 평행사변형 못만든다
if (yb-ya)*(xc-xb)==(xb-xa)*(yc-yb):
    print(-1.0)
else:
    d1 = dist(xa,ya,xb,yb) # a-b사이 거리
    d2 = dist(xb,yb,xc,yc) # b-c사이 거리
    d3 = dist(xc,yc,xa,ya) # c-a사이 거리
    print(2*(max(d1,d2,d3)-min(d1,d2,d3)))