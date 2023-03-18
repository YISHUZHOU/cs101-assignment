with open('./test_Docker1_result.txt', 'w') as f:
    print('Hello World!', file=f)

# 导入pandas模块
import pandas as pd
# 导入numpy模块
import numpy as np

# 创建一个dataframe
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
# 将dataframe写入csv文件
df.to_csv('./test_Docker2_result.csv')
# 将dataframe写入excel文件
# 创建一个20行30列的dataframe，数字随机
df = pd.DataFrame(np.random.randn(20, 30))
# 写入excel文件
df.to_excel('./test_Docker3_result.xlsx')

# 导入matplotlib模块
import matplotlib.pyplot as plt
#把df输出成折线图

df.plot()