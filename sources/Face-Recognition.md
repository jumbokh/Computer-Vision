## pip install opencv-python numpy face-recognition pillow
## source: https://github.com/ageitgey/face_recognition
## Intrustion in CN-Chinese: https://github.com/ageitgey/face_recognition/blob/master/README_Simplified_Chinese.md
### Prequirements:
* cmake
  ```
  Cmake 下載安裝方法
在這裡下載 https://cmake.org/download/
選擇Windows win64-x64 ZIP
完成後放在資料夾整理好並解壓縮
打開解縮檔->bin資料夾
複製路徑(之後要用)
開啟"系統內容"(步驟:按win+R，輸入sysdm.cpl)
點選進階->環境變數
進去後點選在系統變數底下的Path->點選編輯
新增->貼上之前複製好的路徑
確定後關閉
  ```
* dlib
### Download dlib
![pre build Dlib](https://github.com/jumbokh/Computer-Vision/blob/main/images/Download-dlib.png)
### http://dlib.net/compile.html
```
cd examples
mkdir build
cd build
cmake ..
cmake --build . --config Release
```
### 以上做法生成有限制
```
note that when using Visual Studio, CMake will by default generate a 32bit executable. 
This means the programs you compile will only be able to use 2GB of RAM. 
To avoid this, you need to tell CMake to generate a 64bit executable. 
You do this by using a command like
```
```
cmake -G "Visual Studio 14 2015 Win64" -T host=x64 ..
```
