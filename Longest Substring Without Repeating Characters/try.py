def SahilSit(C1,C2):
    return 'C1' if sum(C1) > sum(C2) else 'C2'
    
n=int(input())
res=[]
while(n>0):
    a,b = [int(x) for x in input().split()[:2]]
    C1 = [int(x) for x in input().split()[:a]]
    C2 = [int(x) for x in input().split()[:b]]
    res.append(SahilSit(C1,C2))
    n-=1
for r in res:
    print(r)
