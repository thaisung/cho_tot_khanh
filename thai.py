from datetime import datetime

token_exp = 1702198883  # Giả sử đây là giá trị exp từ payload
current_time = datetime.utcnow().timestamp()  # Lấy thời điểm hiện tại dưới dạng epoch time

if current_time > token_exp:
    print("Token đã hết hạn.")
else:
    print("Token vẫn còn hiệu lực.")
