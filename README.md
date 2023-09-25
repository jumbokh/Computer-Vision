
### [opencv Window 程式安裝說明](https://github.com/jumbokh/Computer-Vision/blob/main/docs/opencv_windows.pdf)
### [AlphaNum dataset](https://www.kaggle.com/datasets/lopalp/alphanum)
### git clone https://github.com/jumbokh/Computer-Vision
### pip install matplotlib
```
import cv2
img=cv2.imread("test.bmp")
rows,cols=img.shape[:2]
size=(int(cols*0.9),int(rows*0.5))
rst=cv2.resize(img,size)
print("img.shape=",img.shape)
print("rst.shape=",rst.shape)
```
```
週次 3-4：YOLO 物件偵測
物件偵測概述與挑戰
YOLO 簡介與架構
模型訓練與資料集準備
偵測結果後處理與後續應用
YOLO 在實務中的應用
```
* [Week 1,2 Source](https://github.com/jumbokh/Computer-Vision/blob/main/sources/wk1-2.zip)
* [Week 2 source](https://github.com/jumbokh/Computer-Vision/blob/main/sources/0918.zip)
* [Week 3 09/23](https://github.com/jumbokh/Computer-Vision/tree/main/sources/0923)
* ![grey](https://github.com/jumbokh/Computer-Vision/blob/main/images/wall-greyscale.png)
* ![hist](https://github.com/jumbokh/Computer-Vision/blob/main/images/histogram.png)
### [關於執行原則](https://learn.microsoft.com/zh-tw/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3)
* 開啟 power-shell 執行: set-executionpolicy remotesigned
### python version switch
* sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1
* sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2
* sudo update-alternatives --config python 
### CV2 in Google 
```
from google.colab.patches import cv2_imshow
cv2_imshow(image)
```
### Darknet 
* cv2 not found
```
/src/image_opencv.cpp:5:10: fatal error: opencv2/opencv.hpp: 沒有此一檔案或目錄
```
* [debug opencv for darknet not found](https://github.com/jumbokh/Computer-Vision/blob/main/darknet-opencv.md)
### Notebooks
* [Keras DL](https://github.com/jumbokh/ML-Class/blob/main/notebooks/Ch20_Keras_DL.ipynb)https://github.com/jumbokh/rpi_class/tree/master/lite_install
* [02_1_用CNN圖形辨識](https://github.com/jumbokh/Computer-Vision/blob/main/notebooks/02_1_%E7%94%A8CNN%E5%9C%96%E5%BD%A2%E8%BE%A8%E8%AD%98-%E9%82%84%E6%98%AFMNIST.ipynb)
* [Lab4 bad](https://github.com/jumbokh/ML-Class/blob/main/notebooks/Lab4_bad.ipynb)
* [cifar10-tensorflow](https://github.com/jumbokh/ML-Class/blob/main/notebooks/cifar10-tensorflow.ipynb)
* [image classification](https://github.com/jumbokh/csu1111-class/blob/main/computerVision/notebooks/image_classification.ipynb)
* [YOLO Keras conversion](https://github.com/jumbokh/nknu-class/blob/main/CNN/YOLO/08_05_YOLO_Keras_Conversion.ipynb)
* [YOLO_Keras_Test](https://github.com/jumbokh/nknu-class/blob/main/CNN/YOLO/08_06_YOLO_Keras_Test.ipynb)
* [CNN Notebooks](https://github.com/jumbokh/nknu-class/tree/main/CNN/notebooks)
* [Kaggle: Download Dataset](https://www.kaggle.com/code/surajdidwania/dataset-download)
### ubuntu virtual box
* [Oracle virtual box download](https://www.virtualbox.org/wiki/Downloads)
* [ubuntu download](https://www.ubuntu-tw.org/modules/tinyd0/)
* [python3.8 install](https://www.linuxcapable.com/install-python-3-8-on-ubuntu-linux/)
```
Username: osboxes
Password: osboxes.org
Gust Tools: Installed
Keyboard Layout: US (Qwerty)
VMware Compatibility: Version 10+
```
### [ubuntu setup](https://github.com/jumbokh/rpi_class/tree/master/lite_install)
### 參考網頁
* [蔡炎龍老師MOOC](https://github.com/yenlung/Deep-Learning-MOOC)
* [蔡炎龍老師 深度學習基礎](https://github.com/jumbokh/Deep-Learning-Basics)
* [陳昭明老師 書本範例](https://github.com/mc6666/DL_Book)
* [Deep Learning Keras](https://github.com/erhwenkuo/deep-learning-with-keras-notebooks)
* [YOLO 官網](https://pjreddie.com/darknet/yolo/)
* [使用Haar Cascade 进行人脸识别](https://blog.csdn.net/wutao1530663/article/details/78294349)
* [Image dataset of Symbols](https://www.kaggle.com/datasets/kentvejrupmadsen/letter-images-dataset?resource=download)
* [AlphaNum Dataset](https://www.kaggle.com/datasets/lopalp/alphanum)
* [How Do Computers Store Images?](https://www.analyticsvidhya.com/blog/2021/03/grayscale-and-rgb-format-for-storing-images/)
* [Leveraging Embeddings and Clustering Techniques in Computer Vision](https://blog.roboflow.com/embeddings-clustering-computer-vision-clip-umap/)
* [Loading Data Using Numpy](https://www.kaggle.com/code/thomasqazwsxedc/loading-data-using-numpy)
* [二值化黑白影像](https://steam.oxxostudio.tw/category/python/ai/opencv-threshold.html)
* [直方圖與長條圖](https://www.finereport.com/tw/data-analysis/how-to-make-histogram.html)
* [train_yolo_with_custom_dataset_on_colab_101](https://github.com/wallat/train_yolo_with_custom_dataset_on_colab_101/tree/master)
* [YOLOv4手把手實作應用](https://suyenting.github.io/post/yolov4-hands-on/)
* [國產瑞昱ic 智慧儀表工業應用AMB82 Mini(Realtek Ameba Pro2) & HUB8735 (Detection Meter)](https://www.youtube.com/watch?v=CABstojtbTY)
* [鄉下老師 - 車牌辨識](https://blog.udn.com/mobile/yccsonar/179871458?fbclid=IwAR2MbzmN8VdU6PYTfhPK9rB41JwKRL7CmOxKOpK0oVyVjstS5cvdMgg4qVo)
### 參考文件
* [tensorflow2](https://github.com/jumbokh/csu1111-class/blob/main/computerVision/tensorflow2.pdf)
* [動手學深度學習](https://github.com/jumbokh/csu1111-class/blob/main/computerVision/%E5%8B%95%E6%89%8B%E5%AD%B8%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92.pdf)
* [深度學習最佳入門邁向AI專題實戰 ppt](https://github.com/jumbokh/csu1111-class/blob/main/computerVision/%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92%E6%9C%80%E4%BD%B3%E5%85%A5%E9%96%80%E9%82%81%E5%90%91AI%E5%B0%88%E9%A1%8C%E5%AF%A6%E6%88%B0_%E6%95%99%E5%AD%B8%E8%B3%87%E6%BA%90_2_V1.pptx)
* [到 nvidia 官網下載 CUDA](https://developer.nvidia.com/cuda-toolkit-archive)
#### 實驗材料
* [彩色球](https://drive.google.com/drive/folders/1zDaFGZ5le9AYqT0UhLoMsCDrJJtWu6j3?usp=share_link)
* [AI web -- Teachable Machine](https://teachablemachine.withgoogle.com/)
#### 書目
* ![1921](https://github.com/jumbokh/Computer-Vision/blob/main/images/DM1921_3D_official.jpg)
* ![2201](https://github.com/jumbokh/Computer-Vision/blob/main/images/DM2201_3D-500.jpg)
* ![2311](https://github.com/jumbokh/Computer-Vision/blob/main/images/DM2311_%E7%AB%8B%E9%AB%94%E6%9B%B8_500x500.jpg)
