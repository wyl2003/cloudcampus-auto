# cloudcampus-auto
Python实现cloudcampus云课堂自动点击

---
### Step 1 安装链接抓取插件 Link Grabber
从[chrome应用商店](https://chrome.google.com/webstore/detail/link-grabber/caodelkhipncidmoebgbbeemedohcdma)或其他渠道安装用来抓取练习及文件链接的浏览器插件[Link Grabber](https://github.com/7fffffff/linkgrabber)
### Step 2 选取有效链接并保存
在课程页面下展开所有Navigation,并运行Link Grabber获得整个页面包含的链接

<img width="1415" alt="image" src="https://github.com/wyl2003/cloudcampus-auto/assets/108109393/d966bf8e-c266-4814-831e-45634772f3c2">

练习的链接一般包含**h5pactivity**关键字,搜索此关键字,复制链接保存到`url.txt`  
如果你还希望完成文件点击任务,自行寻找文件链接包含的关键字搜索并保存到`furl.txt`
### Step 3 下载代码及安装库
使用以下命令安装selenium和xlwt库
```
$ pip install selenium xlwt
```
把代码克隆到本地(或者直接下载zip)
```
$ git clone https://github.com/wyl2003/cloudcampus-auto
```
### Step 4 运行代码
把`url.txt`或`furl.txt`放入同一文件夹,并运行相应程序
```
#已准备url.txt 完成练习
$ python CCExercise.py

#已准备furl.txt 完成文件任务
$ python CCFile.py
```
