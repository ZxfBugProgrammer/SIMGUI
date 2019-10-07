# -*-coding=utf8-*-
import os
from pypinyin import lazy_pinyin


def rename(path):
    fileList = os.listdir(path)  # 获取path下所有的文件（包括文件夹）

    for nowFile in fileList:  # 遍历所有文件

        nowFileDir = os.path.join(path, nowFile)  # 原来的文件路径
        if os.path.isdir(nowFileDir):  # 如果是文件夹则跳过
            continue

        fileName, fileType = os.path.splitext(nowFile)  # 获取文件名
        # 把文件名里的汉字转换成其首字母
        fileName = ''.join(lazy_pinyin(fileName, errors='default'))

        newFileDir = os.path.join(path, fileName + fileType)  # 新的文件名

        os.rename(nowFileDir, newFileDir)  # 重命名


if __name__ == '__main__':
    rename(os.getcwd())
