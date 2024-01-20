import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 读取Excel文件
df = pd.read_excel('clustered_data.xlsx')

# 修改 'Cluster' 字段的值
df['Cluster'] = df['Cluster'].map({0: 2, 1: 0, 2: 1})

# 保存修改后的数据到新的Excel文件
df.to_excel('modified_cluster_data.xlsx', index=False)

# 选择用于绘图的字段
fields = ['ICTApp', 'ICTUse', 'ICTCmp']

# 三维散点图可视化
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 不同聚类的颜色
colors = ['blue', 'green', 'orange']
cluster_labels = ['Cluster 0', 'Cluster 1', 'Cluster 2']

for i in range(3):
    ax.scatter(df[df['Cluster'] == i][fields[0]],
               df[df['Cluster'] == i][fields[1]],
               df[df['Cluster'] == i][fields[2]],
               c=colors[i],
               label=cluster_labels[i])

ax.set_xlabel(fields[0])
ax.set_ylabel(fields[1])
ax.set_zlabel(fields[2])
ax.set_title('3D Scatter Plot of ICT Fields by Cluster')

# 添加图例
ax.legend()

# 保存图像
plt.savefig('3d_scatter_plot.png')

plt.show()
