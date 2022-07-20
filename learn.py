#from itertools import permutations
from collections import Counter

for i in range(int(input())):
    a, b = input().strip().split()
    parent = a + b
    parentCounter=Counter(parent)
    child = ""
    for i in range(int(input())):
        child+=input().strip()
    childCounter=Counter(child)

    ans = ""
    for i in childCounter:
        if i not in parentCounter.keys():
            ans = "NO"
            break
        else:
            if childCounter[i]>parentCounter[i]:
                ans = "NO"
                break
            else:
                ans = "YES"
    print(ans)