import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# 读取Excel文件
df = pd.read_excel('modified_cluster_data.xlsx')

# 为每个Cluster准备一个空的字典来存储结果
results_dict = {}

# 对每个Cluster进行多元线性回归
for cluster in sorted(df['Cluster'].unique()):
    subset = df[df['Cluster'] == cluster]
    model = ols('y ~ ICTApp + ICTUse + ICTCmp', data=subset).fit()

    # 提取并存储回归统计数据
    results = [model.params['Intercept']] + list(model.params[1:]) + \
              [model.rsquared, len(subset), model.fvalue] + \
              [model.pvalues['Intercept']] + list(model.pvalues[1:])
    results_dict[cluster] = results

# 转换字典为DataFrame
results_df = pd.DataFrame(results_dict)

# 设置行索引
results_df.index = ["Intercept", "ICTApp", "ICTUse", "ICTCmp", "R-Squared", "N", "F-Statistic",
                    "P-Value Intercept", "P-Value ICTApp", "P-Value ICTUse", "P-Value ICTCmp"]

# 保存结果到新的Excel文件
results_df.to_excel('regression_results2.xlsx')
