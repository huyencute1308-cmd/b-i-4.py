s = input("Nhập các số cách nhau bởi dấu phẩy: ")
numbers = [int(x) for x in s.split(',')]
odd_numbers = [x for x in numbers if x % 2 == 1]

print("Các số lẻ:", ','.join(map(str, odd_numbers)))


