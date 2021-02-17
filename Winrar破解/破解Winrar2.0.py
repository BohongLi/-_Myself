# -*- codeing =utf-8 -*-
# @Time: 2021/2/3 17:41
# @Author : BohongLi
# @File : 破解Winrar2.0.py
# @Software : PyCharm
import os
import sys
import datetime
from unrar import rarfile


def baopo(wenjian):
    bfound = False
    fp = rarfile.RarFile(wenjian)
    start = 0
    stop = 9999
    for i in range(start, stop):
        a = str(i).zfill((4))
        try:
            fp.extractall(path="./aaa", pwd=a)
            print("\n爆破成功，密码：" + a)
            bfound = True
            fp._close(wenjian)
        except Exception as e:
            print("\r已尝试", '{:.0%}'.format((i - start) / (stop - start)), end="")
        if bfound:
            break


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    baopo(sys.argv[1])
    endtime = datetime.datetime.now()
    print("共耗时", (endtime - starttime).seconds, "秒")
