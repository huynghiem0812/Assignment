from collections import Counter

n = int(input())
l = list()
for _ in range(n):
    l.append(input())
x = Counter(l)
print(len(x))
print(*x.values())
