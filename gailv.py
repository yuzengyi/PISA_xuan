import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('modified_cluster_data.xlsx')

# 计算每个聚类类别的总数
cluster_counts = df['Cluster'].value_counts()
print("每个聚类类别的总数:")
print(cluster_counts)

# 计算'DigMat'为1的概率
probabilities = df.groupby('Cluster')['DigMat'].mean()
print("\n不同聚类类别中'DigMat'为1的概率:")
print(probabilities)

# 绘制柱状图
probabilities.plot(kind='bar')
plt.title("Probability of 'DigMat' = 1 by Cluster")
plt.xlabel('Cluster')
plt.ylabel('Probability')
plt.xticks(rotation=0)  # 将x轴标签设为水平

# 保存图像
plt.savefig('digmat_probability_by_cluster.png')

plt.show()
