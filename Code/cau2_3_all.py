import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Sử dụng backend không cần giao diện

import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Excel với tên cột ở hàng thứ 3
file_path = 'results.csv'
df = pd.read_csv(file_path, header=2)

# Loại bỏ các cột không cần thiết
df = df.drop(columns=['Unnamed: 0', 'Rk'], errors='ignore')  # 'errors=ignore' để không gây lỗi nếu cột không tồn tại

# Chọn chỉ các cột số
numeric_columns = df.select_dtypes(include=['float', 'int']).columns

# Thiết lập số lượng hàng và cột cho subplots
n_columns = 3  # Số cột trong subplot
n_rows = (len(numeric_columns) + n_columns - 1) // n_columns  # Tính số hàng cần thiết

# Tạo figure và axes
fig, axes = plt.subplots(n_rows, n_columns, figsize=(15, n_rows * 4))  # Điều chỉnh kích thước hình ảnh
axes = axes.flatten()  # Chuyển đổi axes thành mảng 1 chiều

# Vẽ histogram cho từng cột số
for i, column in enumerate(numeric_columns):
    axes[i].hist(df[column].dropna(), bins=10, edgecolor='black')  # Loại bỏ NaN để tránh lỗi
    axes[i].set_title(f'Histogram phân bố cho {column}')
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Player')

# Ẩn các axes không sử dụng
for j in range(i + 1, len(axes)):
    axes[j].axis('off')  # Ẩn các axes không cần thiết thay vì xóa để giữ layout nhất quán

# Lưu tất cả histogram vào một file ảnh
plt.tight_layout()  # Căn chỉnh layout
plt.savefig("all_histograms.png", dpi=300)  # Lưu file ảnh với độ phân giải cao
print("Lưu tất cả histogram vào all_histograms.png")
plt.close()  # Đóng hình sau khi lưu
