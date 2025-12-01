result = []
for i in range(1000, 3001):
    s = str(i)
    if all(int(d)%2==0 for d in s):
        result.append(s)

print(','.join(result))


