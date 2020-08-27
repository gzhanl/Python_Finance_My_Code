# =============================================================================
# 7.3.1 相关系数基础 by 王宇韬&肖金鑫
# =============================================================================

# 注意，在下面的代码运行过程中，如果是用pycharm运行程序，需要把生成的图片关掉，才能继续执行下面的程序

import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

x = np.arange(0, 10, 0.2)  # 生成0-10的一维数组，间隔为0.2
y1 = 3 * x + 5

# y2在y1的基础上进行-5和5之间随机实数波动
y2 = []
for i in y1:
    y2.append(i + random.uniform(-5, 5))

plt.plot(x, y1, color='r', label='y1')
plt.plot(x, y2, linestyle='--', label='y2')
plt.legend(loc='upper left')
plt.show()


corr = pearsonr(y1, y2)
print('相关系数r值为' + str(corr[0]) + '，显著性水平P值为' + str(corr[1]))