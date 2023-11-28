import seaborn as sns
import matplotlib.pyplot as plt

# 加载 Seaborn 自带的示例数据集 "tips"
tips = sns.load_dataset("tips")

# 绘制散点图
plt.figure(figsize=(8, 4))
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title('散点图')
plt.xlabel('总消费金额')
plt.ylabel('小费金额')

# 绘制柱状图
plt.figure(figsize=(8, 4))
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('柱状图')
plt.xlabel('星期几')
plt.ylabel('总消费金额')

# 绘制箱线图
plt.figure(figsize=(8, 4))
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title('箱线图')
plt.xlabel('星期几')
plt.ylabel('总消费金额')

# 显示图形
plt.tight_layout()
plt.show()