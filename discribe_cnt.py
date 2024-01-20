import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取Excel文件
df = pd.read_excel('converted_data.xlsx')  # 替换 'your_file.xlsx' 为您的文件路径

# 分别筛选出'HKG'和'MAC'地区的数据
df_hkg = df[df['Cnt'] == 'HKG']
df_mac = df[df['Cnt'] == 'MAC']

# 对'HKG'地区的数据进行随机抽样，以匹配'MAC'地区的样本大小
sample_size = len(df_mac)
df_hkg_sampled = df_hkg.sample(n=sample_size, random_state=1)

# 合并调整后的'HKG'数据和'MAC'数据
df_combined = pd.concat([df_hkg_sampled, df_mac])

# 使用Seaborn绘制分布图
plt.figure(figsize=(10, 6))
sns.histplot(data=df_combined, x='y', hue='Cnt', kde=True, element='step')
plt.title('Adjusted Distribution of y in HKG and MAC Regions')
plt.xlabel('y Value')
plt.ylabel('Frequency')
plt.savefig('distribution_plot.png')
plt.show()
