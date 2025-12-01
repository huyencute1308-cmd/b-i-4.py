n = int(input("Nhập n: "))

fib = [0, 1]
while fib[-1] + fib[-2] < n:
    fib.append(fib[-1] + fib[-2])

print("Các số Fibonacci nhỏ hơn n:", fib)

