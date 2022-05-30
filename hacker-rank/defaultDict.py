from collections import defaultdict

n,m = list(map(int,input().split()))
ddiccio = defaultdict(list)

while n:
    ddiccio["A"].append(input())
    n -= 1
while m:
    ddiccio["B"].append(input())
    m -= 1

for i in ddiccio["B"]:
    if i in ddiccio["A"]:
        for j,k in enumerate(ddiccio["A"]):
            if i == k:
                print(j+1,end=" ")
        print()
    else:
        print(-1)
