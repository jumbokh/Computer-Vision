# ch19_4.py
import matplotlib.pyplot as plt
import numpy as np

freq = [2/9, 1/9, 2/9, 1/9, 3/9]    # 出現頻率
N = len(freq)                       # 計算長度
x = np.arange(N)                    # 長條圖x軸座標
width = 0.35                        # 長條圖寬度
plt.bar(x, freq, width)             # 繪製長條圖

plt.xlabel("Pixel Value")           # 像素值
plt.ylabel("Freqency")              # 出現頻率
plt.xticks(x, ('1', '2', '3', '4', '5'))
plt.show()


