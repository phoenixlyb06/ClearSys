# -*- coding: utf-8 -*-
import os
# 遍历文件夹
def DelDirFile(path):
    d = {}
    for root, dirs, files in os.walk(path):
        for f in files:
          file_path = os.path.join(root, f)
          print("del " + file_path)
          if os.path.exists(path):
            try:
                os.remove(file_path)
            except :
                continue

        for d in dirs:
            dir_path = os.path.join(root, d)
            DelDirFile(dir_path)


if __name__ == "__main__":
    env = os.environ
    tmp = env['temp']
    print(tmp)
    DelDirFile(tmp)##tmp 目录该是一些都没用的
    DelDirFile("C:\\Windows\\Temp")
    #还有啥？？