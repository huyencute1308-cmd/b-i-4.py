s = input("Nhập câu: ")

upper_count = sum(c.isupper() for c in s)
lower_count = sum(c.islower() for c in s)

print("Chữ hoa:", upper_count)
print("Chữ thường:", lower_count)

