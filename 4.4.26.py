balance = 0

while True:
    try:
        line = input("Nhập giao dịch (hoặc nhấn Enter để kết thúc): ")
        if not line:
            break
        parts = line.split()
        if parts[0] == 'D':
            balance += int(parts[1])
        elif parts[0] == 'W':
            balance -= int(parts[1])
    except:
        print("Định dạng không hợp lệ, thử lại.")

print("Số dư thực:", balance)

