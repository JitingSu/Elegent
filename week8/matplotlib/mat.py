import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据集
x = np.linspace(0, 10, 100)  # 生成0到10的100个均匀分布的数据点
y = np.sin(x)  # 计算每个数据点的正弦值
data_points = np.random.rand(50, 2)  # 生成50个随机散点数据点
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 40, 30, 55]

# 绘制折线图
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Sine Wave', color='blue', linestyle='-', linewidth=2)
plt.title('折线图')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.legend()
plt.grid(True)

# 绘制散点图
plt.figure(figsize=(8, 4))
plt.scatter(data_points[:, 0], data_points[:, 1], label='随机散点', color='green', marker='o')
plt.title('散点图')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.legend()
plt.grid(True)

# 绘制柱状图
plt.figure(figsize=(8, 4))
plt.bar(categories, values, color='orange')
plt.title('柱状图')
plt.xlabel('类别')
plt.ylabel('数值')
plt.grid(axis='y')

# 显示图形
plt.tight_layout()  # 自动调整子图布局
plt.show()