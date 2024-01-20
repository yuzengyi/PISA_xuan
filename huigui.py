import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# 读取Excel文件
df = pd.read_excel('modified_cluster_data.xlsx')

# 初始化一个空的DataFrame来存储结果
results_df = pd.DataFrame()

# 对每个Cluster进行多元线性回归
for cluster in df['Cluster'].unique():
    subset = df[df['Cluster'] == cluster]
    model = ols('y ~ ICTApp + ICTUse + ICTCmp', data=subset).fit()

    # 提取回归统计数据
    params = model.params
    pvalues = model.pvalues
    r_squared = model.rsquared
    n = len(subset)
    f_statistic = model.fvalue

    # 将结果存储到DataFrame中
    temp_df = pd.DataFrame({'Cluster': cluster, 'Coefficient': params.index,
                            'Value': params.values, 'P-Value': pvalues.values})
    temp_df['R-Squared'] = r_squared
    temp_df['N'] = n
    temp_df['F-Statistic'] = f_statistic

    results_df = pd.concat([results_df, temp_df])

# 重置索引
results_df.reset_index(drop=True, inplace=True)

# 保存结果到新的Excel文件
results_df.to_excel('regression_results1.xlsx', index=False)
