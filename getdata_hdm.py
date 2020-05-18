import re
def hdm(file_name):
    """
    功能：得到指定路径的HDM字典数据
        HDM字典数据结构
            桩号key  [[左侧地面线数据]
                    [右侧地面线数据]]
    例句如下：
        filename = r'e:\a\A.hdm'
        s = hdm(filename)
        print(s)
        s2 = s['6255.031']
        s_z_x = s2[0][1::2][0]  #左侧地面线数据x值
        s_z_y = s2[0][2::2][0]  #左侧地面线数据y值
        print(s_z_x)
        print(s_z_y)
    """
    p = re.compile('\s+')  # \s匹配任意空白字符，等价于 [\t\n\r\f]，+表多个
    hdm_dic = {}
    try:
        with open(file_name, encoding='utf-8') as file_obj:
            while True:  # True首字母要大写
                content = file_obj.readline()
                if not content:
                    break
                numofstr = re.sub(p, '', content)
                content=content.split('\t')
                #删除空字符
                new = []
                i = 0
                for temp in content:
                    content[i] = re.sub(p, '', temp)
                    if content[i]:
                        new.append(content[i])
                    i += 1
                content = new
                if len(numofstr) > 0 and len(content)==1:
                    file_content = []
                    hdm_key = re.sub(p,'',content[0])   # 获取到桩号
                else:
                    if len(content)> 1:
                        file_content.append(content)
                        hdm_dic[hdm_key] = file_content # 将HDM数据放入字典
        return hdm_dic
    except FileNotFoundError:
        print(f'{file_name} 这个文件不存在')
