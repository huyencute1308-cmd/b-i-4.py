s = input("Nhập câu: ")
letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)

print("Số chữ cái:", letters)
print("Số chữ số:", digits)

