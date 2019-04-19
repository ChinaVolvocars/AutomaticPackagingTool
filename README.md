# AutomaticPackagingTool
Android 自动打渠道包工具


### 打包操作流程


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

```
{"ret":0,"msg":"ok","isV2":true,"isV2OK":true} 是 V2 签名的App
{"ret":0,"msg":"ok","isV2":false,"isV2OK":false} 不是 V2 签名的App

```

#### **5.** 写入渠道包信息:
```
java -jar [刚下载walle-cli-all.jar的路径] batch -f [项目里channel的路径]  [apk路径]
```

#### **6.** 获取渠道信息

```
String channel = WalleChannelReader.getChannel(context);

```


