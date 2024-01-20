import pandas as pd

# 定义映射关系(组中值)
mapping = {1: 0, 2: 1.5, 3: 18, 4: 72, 5: 180}

# 读取Excel文件
df = pd.read_excel('data.xlsx')

# 对指定列进行转换
columns_to_convert = ['CalcFr', 'EqSolv', 'SimMod', 'CodAlg']
for column in columns_to_convert:
    df[column] = df[column].map(mapping)

# 将转换后的DataFrame导出为新的Excel文件
df.to_excel('converted_data.xlsx', index=False)
