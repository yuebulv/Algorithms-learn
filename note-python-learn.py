##处理异常
"""
    try语句
        try:
            代码块（可能出错的语句）
        except [异常类型]:
            #如果except后不跟任何内容，此时会捕捉到所有异常
            #如果except后加了异常类型，此时只会捕捉该类型的异常
            代码块（出错后处理方式）
        except [异常类型]:
            代码块（出错后处理方式）
        except [异常类型] as 异常名:
            代码块（出错后处理方式）
        else:
            代码块（没出错时要执行的语句）
        finally:
            代码块（该代码总会执行）

        #exception 是所有异常类的父类，所以如果except后跟的是exception，他也会捕捉到所有异常
        #可以在异常类后边跟着一个as xx 此时xx就是异常对象
        except exception as xx:
            print('未知异常'，xx.type(e))
"""
#抛出异常
"""
    raise 异常类型
    raise exception('异常说明')
    #也可以自定义异常类，只需要创建一个类继承exception即可
    class Myerror(exception):
        pass
"""
#操作文件
"""
    1.open
        file_obj=open(file)
        file_obj.close()
    2.with as
        with open(file_name) as file_obj:
            print (file_obj.red())
            #此时这个文件只能在with中使用，一旦with结束则文件自动close()
    #调用open()来打开一个文件，可以将文件分成两种类型
    #一种是纯文本文件（使用uft-8等编码编写的文本文件）
    #一种是二进制文件（图片、MP3、PPT等这些文件）
    #open()打开文件时，默认是以文本文件的形式打开的，但是默认的编码为none
    #所以处理文本文件时，必须要指定文件的编码
        with open(file_name,encoding='utf-8') as file_obj:
    #在windows系统使用路径时，可以使用/来代替\
    #或者可以使用\\来代替\
    #或者也可以使用原始字符串
    file_name ='hello\\demo.txt'
    file_name=r‘hello\demo.txt’
    #表示路径，可以使用..来返回上一级目录
    file_name='../hello/demo.txt'
"""
#读取文件
file_name = r'F:\mysql\A.tf'
try:
    with open(file_name, encoding='utf-8') as file_obj:
        file_content = ''
        chunk = 100
        while True:#True首字母要大写
            content = file_obj.read(chunk)
            #read()读取文件全部内容
            #read(size),这样read每次读取指定size数量的字符，默认值是-1（即全部字符）
            #read每一次读取都是从上次读取的位置开始读取的
            if not content:
                break
            print(content, end='')
            file_content += content
        # readline()
        #该方法可以用来读取一行内容
        print(file_obj.readline(),end='')
        # readlines()
        #该方法用于一行一行的读取内容，它会一次性将读取到的内容封装到一个列表中返回
        # r=file_obj.readlines()
        # pprint.ppint(r[0])#需要import ppint
except FileNotFoundError:
    print(f'{file_name} 这个文件不存在')
#读取文件
file_name = 'demo.txt'
try:
    with open(file_name, 'w', encoding='utf-8') as file_obj:
        # w表示是可写的，使用w来写入文件时，如果文件不存在会创建文件，如果文件存在则会截断文件（删除原来文件中的所有内容）
        # a表示追加内容，如果文件不存在会创建文件，如果文件存在则会向文件中追加内容
        # x 用来新建文件，文件存在则会报错
        # +为操作符增加功能
        # r+ 即可读又可写，文件不存在会报错
        # w+/a+ 即可读又可写
        #读取模式
            # t 读取文本文件（默认值），read(size),size是以字符为单位的
            # b 读取二进制文件，read(size),size是以字节为单位的
            # with open(file_name,'rb') as file_obj:
        file_obj.write('aaa\n')  # \n表示自动换行
        # 如果操作的是一个文本文件的话，则write()需要传递一个字符串作为参数
        file_obj.write(str(123))
        # 写入完成以后，该方法会返回写入的字符个数
        r = file_obj.write('今天天气不错')
except FileNotFoundError:
    print(f'{file_name} 这个文件不存在')

#将读取到的文件写出来
file_name = r'F:\2020道路项目\铜梁S107\施工图\3-纬地\A\A.HDMSJ'
with open(file_name,'rb') as file_obj:#以二进制方式读取文件
    new_name='aa.flac'
    with open(new_name,'wb') as new_obj:
        chunk=1024*100
        while True:
            content=file_obj.read(chunk)
            if not content:
                break
            new_obj.write(content)
#读取文件位置
with open(file_name,'rb') as file_obj:
    # seek() 可以修改当前读取的位置
    # seek()需要两个参数
    # 第一个是要切换到的位置
    # 第二个是计算位置的方式
    #   可选值：
    #       0 从头计算，默认值
    #       1 从当前位置计算
    #       2 从最后位置开始计算
    # tell() 方法用来查看当前读取的位置
    file_obj.seek(55)
    file_obj.seek(55,1)
    print(file_obj.read())
    print('当前读取取了-->',file_obj.tell())
#文件的其他操作
import os
r=os.listdir() #获取指定路径的目录结构
r=os.getcwd() #获取当前所有目录
os.chdir('c:/') #切换当前所有目录，相当于cd
os.mkdir('aaa') #在当前路径下创建一个名字了aaa的目录
os.rmdir() #删除目录
os.remove() #删除文件
os.rename('旧名字','新名字') #可以对一个文件进行重命名，也可以用来移动一个文件


# 快速注释代码 (ctrl + /)
#  python规整代码快捷键‘Ctrl + Alt + L