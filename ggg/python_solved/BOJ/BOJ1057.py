N, kjm, ihs = map(int, input().split())

round = 0
while kjm > 0 and ihs > 0:
    round += 1
    kjm = kjm//2 + kjm%2
    ihs = ihs//2 + ihs%2
    if(kjm == ihs):
        break

print(round)