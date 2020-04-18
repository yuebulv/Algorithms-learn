import os
import numpy as np
"""
    #从filename文件中恢复文件名
"""
def renameback(path):
    files = os.listdir(path)
    readestatus = 0
    if os.path.exists(path + '/' + 'filename.txt'):
        for file in files:
            if os.path.isdir(path + '/' + file):
                renameback(path + '/' + file)
            elif os.path.isfile(path + '/' + file) and (file.find('filename.txt')<0):
                if readestatus == 0:
                    with open(path + '/' + 'filename.txt', 'r') as f:  # 读入filename文件名
                        line = f.readline()
                        data_list = []
                        while line:
                            line = line.strip('\n')
                            num = list(line.split('\t'))
                            data_list.append(num)
                            line = f.readline()
                        f.close()
                        all_files = np.array(data_list)
                        lineofall_files = len(all_files)
                        readestatus=1
                for i in range(lineofall_files):
                    if file==all_files[i,1]:
                        os.rename(path + '/' + file, path + '/' + all_files[i,0])
                        break
        readestatus = 0
        return all_files
    # return all_files
list_a = []
path = "F:\\2020-RoadProject\GuiZhou-province\ChishuiCountryroad\\3-hint"
contents = renameback(path)
