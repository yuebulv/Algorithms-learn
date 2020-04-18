import os
import numpy as np
"""
    #从filename文件中恢复文件名
"""
def renamedir(path):
    files = os.listdir(path)
    filenumber=1
    for file in files:
        if os.path.isdir(path + '/' + file):
            # renamedir(path + '/' + file)
            # filenewname = str(filenumber) + "rename"
            # while os.path.exists(path + '/' + filenewname): #判断是否已存在文件名
            #     filenumber += 1
            #     filenewname=str(filenumber)+"rename"
            # os.rename(path + '/' + file, path + '/' + filenewname)
            # with open(path + '/' + 'filename.txt', 'a') as f:#记录文件名
            #     f.write(file+'\t'+filenewname+"\n")
            #     f.close()
            # filenumber += 1

list_a = []
path = "F:\\2020-RoadProject\GuiZhou-province\ChishuiCountryroad\\3-hint"
contents = renamedir(path)