## 報告
* ![報告](https://github.com/jumbokh/Computer-Vision/blob/main/images/%E5%9C%8B%E7%AB%8B%E9%AB%98%E9%9B%84%E5%A4%A7%E5%AD%B8_1.jpg)
## 資料集建立簡介
* [Google ML 基礎課程](https://developers.google.com/machine-learning/data-prep/construct/construct-intro?hl=zh-tw)
* [Build Your Own Face Recognition Tool With Python](https://realpython.com/face-recognition-with-python/)
* [How to quickly build your own dataset of images for Deep Learning](https://medium.com/mlearning-ai/how-to-quickly-build-your-own-dataset-of-images-for-deep-learning-1cf79073f1bd)
* [How to Create a New Custom Dataset from Images](https://pub.towardsai.net/how-to-create-a-new-custom-dataset-from-images-9b95977964ab)
     * [code](https://github.com/Uday47/How-to-create-a-new-custom-dataset-from-images-Medium-Article)
## opencv 影像存取
* [Python 與 OpenCV 基本讀取、顯示與儲存圖片教學](https://blog.gtwang.org/programming/opencv-basic-image-read-and-write-tutorial/)
* [resize](https://github.com/jumbokh/cv_face/blob/master/refers/resize.py)
## 智慧農業
* [芒果分類](https://github.com/jumbokh/Computer-Vision/blob/main/notebooks/AIMango/mango-classification.ipynb)
* [AI Go 芒果分類](https://github.com/jumbokh/Computer-Vision/tree/main/notebooks/AIMango)
* 共享資料:
    * [資料一](https://drive.google.com/file/d/1pCZw19OGsa0lgLlW4NydO2iOcNIqEIPK/view?usp=drive_link)
    * [資料二](https://drive.google.com/file/d/10VpEmE89I-_ChiRvPllDg7gLY4j9BgdO/view?usp=drive_link)
    * [資料三](https://drive.google.com/file/d/17k_A9mqIeYvGyq3bZF_RwQNWdwjYt_Pe/view?usp=drive_link)
## 隧道檢測
* [中寮隧道](https://drive.google.com/drive/folders/1TRWewEYNaMiHborwIAyAmY2WA5S-C8tc?usp=drive_link)
## Teachable Machine
* [Color Ball](https://drive.google.com/file/d/1qDh8T6aB9WAAFRfwDJRi1lXLUuOrbMWh/view?usp=sharing)
* [明星臉](https://drive.google.com/file/d/1nJslbHo9cnmF7OzpuwxxiFUAo6GHSM_t/view?usp=drive_link)
* [蟲](https://drive.google.com/file/d/1eLA5QjxXbGiOl_E_Q_Eq0I8DDGLdYXOf/view?usp=sharing)
## 儀表辨識
* [WE-I Plus 智慧儀錶辨識](https://www.ideas-hatch.com/evb_share_detail.jsp?id=70)
## face_recognition
* [ppt](https://github.com/jumbokh/Computer-Vision/blob/main/docs/Facial_Recognition_PPT.pdf)
* [github](https://github.com/ageitgey/face_recognition)
* [CN](https://github.com/ageitgey/face_recognition/blob/master/README_Simplified_Chinese.md)
* [Book](https://github.com/jumbokh/cv_face/blob/master/refers/Face%20Recognition%20in%20Adverse%20Conditions.pdf)
* ![Dataset Structure](https://github.com/jumbokh/Computer-Vision/blob/main/images/Dataset_struct.JPG)
```
python encode_faces.py --dataset dataset --encodings encodings.pickle
python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png
```
* [github](https://github.com/adityaguptai/Face-Recognition/tree/master)
* [encode_faces](https://github.com/jumbokh/Computer-Vision/blob/main/sources/encode_faces.py)
* [recognize face](https://github.com/jumbokh/Computer-Vision/blob/main/sources/recognize_faces_image.py)
## HAAR 辨識
* [haar](https://github.com/jumbokh/cv_face/tree/master/opencv/day2/haarcascades)
* [Haar Train](https://github.com/jumbokh/cv_face/blob/master/opencv/day3/HAAR_Train_win.md)
* [十行Python代码实现人脸识别](https://zhuanlan.zhihu.com/p/66368987)
* [路標訓練](https://github.com/jumbokh/gcp_class/tree/master/VISION/FT700/ch11)
* [F1700旗標書簡報](https://github.com/jumbokh/cv_face/tree/master/opencv/Book)
## GCP vision
* [Cloud Vision 電腦視覺實戰](https://github.com/jumbokh/gcp_class/tree/master/VISION)
## 胸部x光辨識
* [Pneumonia Detection](https://www.kaggle.com/competitions/pneumonia-detection/overview)
* [Pneumonia Detection by CNN with Data Augmentation](https://github.com/jumbokh/Computer-Vision/blob/main/sources/pneumonia-detection-by-cnn-with-data-augmen-1ddc59.ipynb)
* [Data Preprocessing for Pneumonia Detection](https://github.com/jumbokh/Computer-Vision/blob/main/sources/data-preprocessing-for-pneumonia-detection-437411.ipynb)
* [pneumonia-detection-by-vgg16](https://github.com/jumbokh/Computer-Vision/blob/main/sources/pneumonia-detection-by-vgg16.ipynb)
## 6. Data Augmentation 資料增強
* [Data Augmentation 資料增強](https://chtseng.wordpress.com/2017/11/11/data-augmentation-%E8%B3%87%E6%96%99%E5%A2%9E%E5%BC%B7/)
* [MNIST 模型強化](https://github.com/jumbokh/Computer-Vision/blob/main/notebooks/06_05_Data_Augmentation_MNIST.ipynb)
* [pet 資料增補](https://github.com/jumbokh/Computer-Vision/blob/main/notebooks/06_06_Data_Augmentation_Pets.ipynb)
## 7. 預先訓練的模型(Pre-trained Model)
### 7.1 預先訓練模型的簡介
* [完全採用 VGG 16 預先訓練的模型](https://github.com/jumbokh/Computer-Vision/blob/main/notebooks/07_01_Keras_applications.ipynb)
### 7.2 採用完整的模型
* [圖像相似度比較](https://github.com/jumbokh/Computer-Vision/blob/main/notebooks/07_02_%E5%9C%96%E5%83%8F%E7%9B%B8%E4%BC%BC%E5%BA%A6%E6%AF%94%E8%BC%83.ipynb)
### 7.3 採用部分的模型
* [自訂的輸入層及辨識層(Dense)](https://github.com/jumbokh/Computer-Vision/blob/main/notebooks/07_03_Flower_ResNet.ipynb)
### 7.4 轉移學習(Transfer Learning)
### 7.5 Batch Normalization層
