# AutomaticPackagingTool
Android 自动打渠道包工具，使用 python 3.7 **使用之前必须安装并配置相关环境（Java、Android、Python）**

### 自动化打包操作流程
#### **1.** 在 Android 项目的根目录 build.gradle 文件中添加 Walle Gradle 插件的依赖， 如下：
```gradle
buildscript {
    dependencies {
        classpath 'com.meituan.android.walle:plugin:1.1.6'
    }
}
```

当前 app 的 build.gradle 文件中 apply 这个插件，并添加上用于读取渠道号的AAR
```gradle
apply plugin: 'walle'

dependencies {
    implementation 'com.meituan.android.walle:library:1.1.6'
}
```

通过以下代码获取渠道信息
```java
String channel = WalleChannelReader.getChannel(this.getApplicationContext());
```
#### **2.** 打一个签名的apk
<img src="https://github.com/ChinaVolvocars/AutomaticPackagingTool/blob/master/img/build_apk.png">

#### **3.** 将项目中的 jks 文件、channel 文件（如果没有请新建一个）、打包好的 apk 文件拷贝到 apk 目录里面
<img src="https://github.com/ChinaVolvocars/AutomaticPackagingTool/blob/master/img/copy_file.png">

#### **4.** 在 python 中配置信息
```python
# android_build_tools 路径
android_build_tools_path = 'D:/DevelopmentTools/Android/SDK/build-tools/28.0.0/'
# 生成的文件名
target_file_name = 'AP'
# jks keystore_password
keystore_password = "123456"
# jks 别名
key_alias = "AutomaticPackaging"
# jks key_password
key_password = "123456"
```

#### **5.** 在 include 文件夹中 run 一下就开始批量打包了
<img src="https://github.com/ChinaVolvocars/AutomaticPackagingTool/blob/master/img/run.png">

[Android source](https://github.com/ChinaVolvocars/AutomaticPackaging/)

### 手动打包操作流程


##### **1.** 对齐:
```
Win:zipalign -v 4 source.apk destination.apk

Mac:./zipalign -v 4 source.apk destination.apk
```

##### **2.** 优化:
```
Win:zipalign -c -v 4 destination.apk

Mac:./zipalign -c -v 4 destination.apk
```

#### **3.** 签名
```
Windows: apksigner sign --ks [你的签名文件] [apk路径]

Mac: apksigner sign --ks [你的签名文件] [apk路径]
```

#### **4.** 检查是否使用v2签名:
```
java -jar CheckAndroidV2Signature.jar destination.apk
```

```json
{"ret":0,"msg":"ok","isV2":true,"isV2OK":true} 是 V2 签名的App
{"ret":0,"msg":"ok","isV2":false,"isV2OK":false} 不是 V2 签名的App
```

#### **5.** 写入渠道包信息:
```
java -jar [刚下载walle-cli-all.jar的路径] batch -f [项目里channel的路径]  [apk路径]
```

#### **6.** 获取渠道信息

```java
String channel = WalleChannelReader.getChannel(context);
```


The MIT License (MIT)

Copyright (c) 2015-2019 The ChinaVolvocars Authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
