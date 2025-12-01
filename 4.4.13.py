lst = input("Nhập list: ").split()
x = input("Nhập phần tử cần tìm: ")

if x in lst:
    print("Có trong list, tại vị trí:", lst.index(x))
else:
    print("Không có trong list")
