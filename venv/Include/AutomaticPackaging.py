#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import platform
import shutil
import subprocess
import sys
import json

# 配置
# 打包流程

# 检查是否是 WINDOWS 系统
#     检查 JAVA 环境是否安装
#     检查 Android 环境是否安装
# 检查是否是 MAC 系统
#     检查 JAVA 环境是否安装
#     检查 Android 环境是否安装
# 检查是否是 Ubuntu 系统
#     检查 JAVA 环境是否安装
#     检查 Android 环境是否安装

# 检查ok之后

# 原文件
# 目标文件
# jks 文件
# CheckAndroidV2Signature.jar 路径
# walle-cli-all.jar 路径

platform_platform = platform.platform()
is_windows_platform = 'Windows' in platform_platform
is_linux_platform = 'Linux' in platform_platform
is_macos_platform = 'MacOS' in platform_platform
# D:/DevelopmentTools/Android/SDK/build-tools/28.0.0/
android_build_tools_path = 'D:/DevelopmentTools/Android/SDK/build-tools/28.0.0/'


def current_path():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


enev_path = current_path().split('Include')[0]


def find_target_file_path(rootDir, file_name):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if file_name in path:
            return path
        if os.path.isdir(path):
            find_target_file_path(path)


def different_platforms_backslash():
    if (is_windows_platform):
        return "\\"
    else:
        return "/"


def source_apk_file_path():
    apk_path = find_target_file_path(current_path().split('Include')[0] + 'apk', '.apk')
    return apk_path


def source_target_file_path():
    return current_path().split('Include')[0] + 'apk' + different_platforms_backslash() + 'target_.apk'


def jks_flie_path():
    return find_target_file_path(current_path().split('Include')[0] + 'apk', '.jks')


def channel_flie_path():
    return find_target_file_path(current_path().split('Include')[0] + 'apk', 'channel')


def checkandroidv2signature_flie_path():
    return find_target_file_path(current_path().split('Include')[0] + 'tool', 'CheckAndroidV2Signature.jar')


def walle_cli_all_flie_path():
    return find_target_file_path(current_path().split('Include')[0] + 'tool', 'walle-cli-all.jar')


def out_put_apk_path():
    return current_path().split('Include')[0] + 'out_put_apk'


def check_platform():
    if 'Windows' in platform_platform:
        return 'Windows'
    elif 'Linux' in platform_platform:
        return 'Linux'
    elif 'MacOS' in platform_platform:
        return 'MacOS'
    else:
        return 'Other'


def check_java_env():
    system = os.system('java -version 2>&1 | awk -F[\\\"_] \'NR==1{print $2}\'')
    return system


##### **1.** 对齐:
# ```
# Win:zipalign -v 4 source.apk destination.apk
#
# Mac:./zipalign -v 4 source.apk destination.apk
# ```
def zip_align():
    os.system(android_build_tools_path + "zipalign -v 4 " + source_apk_file_path() + " " + source_target_file_path())


##### **2.** 优化:
# ```
# Win:zipalign -c -v 4 destination.apk
#
# Mac:./zipalign -c -v 4 destination.apk
# ```
def zip_align_optimization():
    os.system(android_build_tools_path + "zipalign -c -v 4 " + " " + source_target_file_path())


#### **3.** 签名
# ```
# Windows: apksigner sign --ks [你的签名文件] [apk路径]
#
# Mac: apksigner sign --ks [你的签名文件] [apk路径]
# ```
keystorePath = jks_flie_path()
keystorePassword = "xxx"
keyAlias = "xxx"
keyPassword = "xxx"


def apksigner_sign():
    # signShell = android_build_tools_path + "apksigner sign --ks "+ keystorePath + " --ks-key-alias " + keyAlias + " --ks-pass pass:" + keystorePassword + " --key-pass pass:" + keyPassword + " --out " + source_target_file_path() + " " + zipalignedApkPath
    signShell = android_build_tools_path + "apksigner sign --ks " + keystorePath + " --ks-key-alias " + keyAlias + " --ks-pass pass:" + keystorePassword + " --key-pass pass:" + keyPassword + " --out " + source_target_file_path() + " " + source_apk_file_path()
    os.system(signShell)


#### **4.** 检查是否使用v2签名:
# ```
# java -jar CheckAndroidV2Signature.jar destination.apk
# ```
def check_android_v2_signature():
    checkV2Shell = "java -jar " + checkandroidv2signature_flie_path() + " " + source_target_file_path();
    system = os.system(checkV2Shell)
    print('检查是否使用v2签名:' + system)


#     {"ret":0,"msg":"ok","isV2":true,"isV2OK":true}


#### **5.** 写入渠道包信息:
# ```
# java -jar [刚下载walle-cli-all.jar的路径] batch -f [项目里channel的路径]  [apk路径]
# ```
def batch_write_channel():
    writeChannelShell = "java -jar " + walle_cli_all_flie_path() + " batch -f " + channel_flie_path() + " " + source_target_file_path() + " " + out_put_apk_path()
    system = os.system(writeChannelShell)


if __name__ == '__main__':
    # print(current_path().split('Include')[0] + 'apk')
    # print(enev_path)
    # print(find_target_file_path(current_path().split('Include')[0] + 'apk', '.apk'))
    # print(source_apk_file_path())
    print(source_target_file_path())
    zip_align()
    zip_align_optimization()
    apksigner_sign()
    check_android_v2_signature()
    batch_write_channel()
