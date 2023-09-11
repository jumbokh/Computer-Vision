### Windows install
* [anaconda](https://www.anaconda.com/download)
### 直接下載安裝
* [官網](https://opencv.org/releases/)
* [參考](https://zhuanlan.zhihu.com/p/629146861)
### conda 虛擬環境安裝
#### [conda env](https://medium.com/python4u/%E7%94%A8conda%E5%BB%BA%E7%AB%8B%E5%8F%8A%E7%AE%A1%E7%90%86python%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83-b61fd2a76566)
```
以系統管理員開啟 anaconda prompt 
執行:
conda update conda
conda env list
conda create --name cv2 python=3.5
conda activate cv2
pip install opencv-python
python -m pip install --upgrade --upgrade pip
(cv2) C:\Users\謝坤達>python -c "import cv2;print(cv2.__version__)"
4.4.0
```
