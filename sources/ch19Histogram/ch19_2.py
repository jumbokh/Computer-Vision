# ch19_2.py
import matplotlib.pyplot as plt
import numpy as np

times = [2, 1, 2, 1, 3]         # 出現次數
N = len(times)                  # 計算長度
x = np.arange(N)                # 長條圖x軸座標
width = 0.35                    # 長條圖寬度
plt.bar(x, times, width)        # 繪製長條圖

plt.xlabel("Pixel Value")       # 像素值
plt.ylabel("Times")             # 出現次數
plt.xticks(x, ('1', '2', '3', '4', '5'))
plt.show()


