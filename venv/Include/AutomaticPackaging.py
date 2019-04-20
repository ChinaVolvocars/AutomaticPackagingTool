#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import platform
import sys
import shutil

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# D:/DevelopmentTools/Android/SDK/build-tools/28.0.0/                                                       
android_build_tools_path = 'D:/DevelopmentTools/Android/SDK/build-tools/28.0.0/'
target_file_name = 'AP'
keystore_password = "123456"
key_alias = "AutomaticPackaging"
key_password = "123456"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

platform_platform = platform.platform()
is_windows_platform = 'Windows' in platform_platform
is_linux_platform = 'Linux' in platform_platform
is_macos_platform = 'MacOS' in platform_platform


def current_path():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


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
    return current_path().split('Include')[0] + 'apk' + different_platforms_backslash() + target_file_name + '.apk'


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


##### **1.** 对齐:
# ```
# Win:zipalign -v 4 source.apk destination.apk
#
# Mac:./zipalign -v 4 source.apk destination.apk
# ```
def zip_align():
    os.system(
        android_build_tools_path + "zipalign -v 4 " + source_apk_file_path() + " " + source_target_file_path())


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
def apksigner_sign():
    jks_path = jks_flie_path()
    # apksigner_sign_shell = android_build_tools_path + "apksigner sign --ks "+ jks_path + " --ks-key-alias " + key_alias + " --ks-pass pass:" + keystore_password + " --key-pass pass:" + key_password + " --out " + source_target_file_path() + " " + source_apk_file_path()
    apksigner_sign_shell = android_build_tools_path + "apksigner sign --ks " + jks_path + " --ks-key-alias " + key_alias + " --ks-pass pass:" + keystore_password + " --key-pass pass:" + key_password + " --out " + source_target_file_path() + " " + source_apk_file_path()
    os.system(apksigner_sign_shell)


#### **4.** 检查是否使用v2签名:
# ```
# java -jar CheckAndroidV2Signature.jar destination.apk
# ```
# {"ret":0,"msg":"ok","isV2":true,"isV2OK":true}
def check_android_v2_signature():
    check_android_v2_signature_shell = "java -jar " + checkandroidv2signature_flie_path() + " " + source_target_file_path();
    system = os.system(check_android_v2_signature_shell)


#### **5.** 写入渠道包信息:
# ```
# java -jar [walle-cli-all.jar的路径] batch -f [项目里channel的路径]  [apk路径]
# ```
def batch_write_channel():
    batch_write_channel_shell = "java -jar " + walle_cli_all_flie_path() + " batch -f " + channel_flie_path() + " " + source_target_file_path() + " " + out_put_apk_path()
    system = os.system(batch_write_channel_shell)


def auto_write_channel():
    if not os.path.exists(source_target_file_path()):
        zip_align()
    else:
        os.remove(source_target_file_path())
        zip_align()

    zip_align_optimization()
    apksigner_sign()
    check_android_v2_signature()

    if not os.path.exists(out_put_apk_path()):
        batch_write_channel()
    else:
        shutil.rmtree(out_put_apk_path())
        batch_write_channel()


if __name__ == '__main__':
    auto_write_channel()
