n = int(input("Nhập n: "))

def sum_of_divisors(x):
    return sum(i for i in range(1, x) if x % i == 0)

for i in range(1, n):
    if sum_of_divisors(i) > i:
        print(i, end=' ')
print()


