s = input("Nhập các số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ")
numbers = s.split(',')
div5 = [num for num in numbers if int(num, 2) % 5 == 0]
print("Các số chia hết cho 5:", ','.join(div5))

