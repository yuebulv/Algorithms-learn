import os
"""
    批量重命名文件名
    命名规则：将含中文文件名/文件夹名转为不含中文文件名/文件夹，并原/现文件名存入filename.txt/dirnewnametxt
"""
def show_files(path, all_files):
    files = os.listdir(path)
    filenumber=1
    firstopenfilename=0
    dirnumber=1
    firstopendirname=0
    for file in files:
        # print(file)
        if os.path.isdir(path + '/' + file):#判断是否为文件夹，并修改文件夹名字
            # print(path + '/' + file)
            show_files(path + '/' + file, all_files)
            if is_contain_chinese(file) :
                dirnewname = str(dirnumber) + "rename"
                while os.path.exists(path + '/' + dirnewname): #判断是否已存在文件名
                    dirnumber += 1
                    dirnewname=str(dirnumber)+"rename"
                os.rename(path + '/' + file, path + '/' + dirnewname)
                if firstopendirname == 0 and os.path.exists(path + '/dirname.txt'):
                    os.remove(path + '/dirname.txt')
                    firstopendirname = 1
                with open(path + '/' + 'dirname.txt', 'a') as f:#记录文件名
                    f.write(file+'\t'+dirnewname+"\n")
                    f.close()
                    firstopendirname = 1
                dirnumber += 1
        elif os.path.isfile(path + '/' + file) and (file.find('filename.txt')<0)and (file.find('dirname.txt')<0)and is_contain_chinese(file) :
            filenewname=file.split(".")
            if len(filenewname)>1:
                filenewname[0] = str(filenumber) + "rename." + filenewname[len(filenewname) - 1]
                while os.path.exists(path + '/' + filenewname[0]): #判断是否已存在文件名
                    filenumber += 1
                    filenewname[0]=str(filenumber)+"rename."+filenewname[len(filenewname)-1]
            else:
                while os.path.exists(path + '/' + filenewname[0]):  # 判断是否已存在文件名
                    filenewname[0] = str(filenumber)+'rename'
                    filenumber += 1
            os.rename(path + '/' + file, path + '/' + filenewname[0])
            all_files.append(path + '/' + filenewname[0])
            if firstopenfilename == 0 and os.path.exists(path + '/filename.txt'):
                os.remove(path + '/filename.txt')
                firstopenfilename = 1
            with open(path + '/' + 'filename.txt', 'a') as f:#记录文件名
                f.write(file+'\t'+filenewname[0]+"\n")
                f.close()
                firstopenfilename = 1
            filenumber += 1
    return all_files

def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

list_a = []
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
path = "F:\\2020-RoadProject\GuiZhou-province\ChishuiCountryroad\\3-hint"
file_path = filedialog.askdirectory()
contents = show_files(path, list_a)
# for content in contents:
#     print(content)