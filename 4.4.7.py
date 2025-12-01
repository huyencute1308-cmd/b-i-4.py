s = input("Nhập chuỗi: ")

ket_qua = ""
for ch in s:
    if not ch.isdigit():     # nếu không phải chữ số
        ket_qua += ch

print("Chuỗi sau khi bỏ chữ số:", ket_qua)



