### Step1 建置 darknet 環境
* [colab darknet](https://github.com/jumbokh/Computer-Vision/blob/main/notebooks/tiny/01_%E5%BB%BA%E7%AB%8BDarknet%E7%B6%B2%E8%B7%AF.ipynb)
### Step2 Labeling data
* ![bread](https://github.com/jumbokh/Computer-Vision/blob/main/images/1.JPG)
### https://app.roboflow.com/jumbokh
* ![bread label](https://github.com/jumbokh/Computer-Vision/blob/main/images/LabelRobotflow.JPG)
### Org Data: 下載：twgo.io/xbiei
###  Download: Bread.v2i.darknet.zip
### step3 資料預處理
* [data process](https://colab.research.google.com/github/jumbokh/Computer-Vision/blob/main/notebooks/tiny/05_darknet_%E8%B3%87%E6%96%99%E9%A0%90%E8%99%95%E7%90%86.ipynb)
### Step4 Trainning
* ![train YOLO](https://github.com/jumbokh/Computer-Vision/blob/main/images/trainYolo.JPG)
* [Train](https://github.com/jumbokh/Computer-Vision/blob/main/notebooks/tiny/06_%E9%96%8B%E5%A7%8B%E8%A8%93%E7%B7%B4.ipynb)
### Step5 Replace weights
```
透過線上轉換檔案格式(YOLO .weights->AMB .nb)
註冊並登入realtech AMB網站
線上轉換網址：https://www.amebaiot.com/zh/amebapro2-ai-convert-model/
可將YOLO模型(.weight, cfg)轉成AMB專屬的.nb檔案

目錄: (取代 yolov4_tiny.nb)
C:\Users\jumbo\AppData\Local\Arduino15\packages\realtek\hardware\AmebaPro2\4.0.4\variants\common_nn_models
```
