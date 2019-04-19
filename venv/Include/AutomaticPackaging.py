#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import platform
import shutil
import subprocess

# 配置
# 打包流程

# 检查是否是windows系统
#     检查java环境是否安装
#     检查Android 环境是否安装
# 检查是否是mac系统
#     检查java环境是否安装
#     检查Android 环境是否安装
# 检查是否是Ubuntu系统
#     检查java环境是否安装
#     检查Android 环境是否安装

# 检查ok之后

platform_platform = platform.platform()


def checkPlatform():
    if 'Windows' in platform_platform:
        return 'Windows'
    elif 'Linux' in platform_platform:
        return 'Linux'
    elif 'MacOS' in platform_platform:
        return 'MacOS'
    else:
        return 'Other'


def checkJavaEnv():
    system = os.system('java -version 2>&1 | awk -F[\\\"_] \'NR==1{print $2}\'')
    return system


if __name__ == '__main__':
    check_platform = checkPlatform()
    print(check_platform)
    env = checkJavaEnv()
    print(env)
