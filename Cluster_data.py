import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 读取Excel文件
df = pd.read_excel('NoCnt_converted_data.xlsx')  # 替换 'your_file.xlsx' 为您的文件路径

# 选择用于聚类的字段
fields = ['ICTApp', 'ICTUse', 'ICTCmp']
X = df[fields]

# 进行聚类，这里选择3个类
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
labels = kmeans.labels_

# 将聚类结果添加到原始DataFrame中
df['Cluster'] = labels

# 保存带有聚类结果的数据到新的Excel文件
df.to_excel('clustered_data.xlsx', index=False)

# 三维聚类结果可视化
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 散点图
scatter = ax.scatter(X.iloc[:, 0], X.iloc[:, 1], X.iloc[:, 2], c=labels, cmap='viridis')

# 聚类中心
centers = kmeans.cluster_centers_
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], c='red', s=100, alpha=0.5, marker='o')

ax.set_xlabel(fields[0])
ax.set_ylabel(fields[1])
ax.set_zlabel(fields[2])
ax.set_title('3D Cluster Visualization')

# 图例
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)

# 保存图像
plt.savefig('3d_plot.png')

plt.show()
