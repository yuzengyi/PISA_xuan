import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取Excel文件
df = pd.read_excel('converted_data.xlsx')  # 替换 'your_file.xlsx' 为您的文件路径

# 筛选出'HKG'和'MAC'地区的数据
df_filtered = df[df['Cnt'].isin(['HKG', 'MAC'])]

# 使用Seaborn绘制分布图
plt.figure(figsize=(10, 6))
sns.histplot(data=df_filtered, x='y', hue='Cnt', kde=True, element='step')
plt.title('Distribution of y in HKG and MAC Regions')
plt.xlabel('y Value')
plt.ylabel('Frequency')
# 保存图表到文件
plt.savefig('No_distribution_plot.png')
plt.show()
