# -*- codeing =utf-8 -*-
# @Time: 2021/2/1 16:39
# @Author : BohongLi
# @File : 破解Winrar.py
# @Software : PyCharm
import os
for i in range(0000,6666):
    cmd = "rar e -y -p%s 破解测试文件.rar" % i
    r=os.system(cmd)
    if r == 0 or r == 1:
        print("Password:%s"%i)
        break
