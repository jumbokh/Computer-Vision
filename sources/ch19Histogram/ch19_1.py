# ch19_1.py
import matplotlib.pyplot as plt

seq = [1, 2, 3, 4, 5]           # 像素值
times = [2, 1, 2, 1, 3]         # 出現次數
plt.plot(seq, times, "-o")      # 繪含標記的圖
plt.axis([0, 6, 0, 4])          # 建立軸大小
plt.xlabel("Pixel Value")       # 像素值
plt.ylabel("Times")             # 出現次數
plt.show()


