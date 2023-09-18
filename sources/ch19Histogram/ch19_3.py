# ch19_3.py
import matplotlib.pyplot as plt

seq = [1, 2, 3, 4, 5]               # 像素值
freq = [2/9, 1/9, 2/9, 1/9, 3/9]    # 出現頻率
plt.plot(seq, freq, "-o")           # 繪含標記的圖
plt.axis([0, 6, 0, 0.5])            # 建立軸大小
plt.xlabel("Pixel Value")           # 像素值
plt.ylabel("Frequency")             # 出現頻率
plt.show()


