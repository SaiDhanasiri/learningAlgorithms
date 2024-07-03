
w1 = input()
w2 = input()
ans = []
lenRange = max(len(w1), len(w2))
i = 0

for x in range(lenRange):
    if i < len(w1):
        ans += w1[i]
    if i < len(w2):
        ans += w2[i]
    i+=1

print(''.join(ans))

