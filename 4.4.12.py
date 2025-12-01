lst = input("Nhập list: ").split()
x = input("Nhập phần tử cần bỏ: ")

if x in lst:
    lst.remove(x)
else:
    print("Không tìm thấy phần tử!")

print("List sau khi bỏ:", lst)
