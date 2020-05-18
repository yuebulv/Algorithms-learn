import pandas as pd
'''
需要手动删除 tf数据前两行数据
需要改进
'''
def tf(filename):
    try:
        data=pd.read_csv(filename,encoding='gbk',header=None,sep='\t')#,sep='\t'
        # data = pd.to_csv(filename, encoding='gbk', header=None, sep='\t')
        # data.drop(data.index[[0,1]], inplace=True)
        data.columns=['桩号','挖方面积','填方面积','中桩填挖','路基左宽','路基右宽',
                      '基缘左高','基缘右高','左坡脚距','右坡脚距','左坡脚高',
                      '右坡脚高','左沟缘距','右沟缘距','左护坡道宽','右护坡道宽',
                      '左沟底高','右沟底高','左沟心距','右沟心距','左沟深度',
                      '右沟深度','左用地宽','右用地宽','清表面积','顶超面积',
                      '左超面积','右超面积','计排水沟','左沟面积填','左沟面积挖',
                      '右沟面积填','右沟面积挖','路槽面积填','路槽面积挖','清表宽度',
                      '清表厚度','挖1类面积','挖2类面积','挖3类面积',
                      '左路槽','右路槽','左路槽',
                      '右路槽','左垫层','右垫层','左路床','右路床',
                      '左土肩培土','右土肩培土','左包边土','右包边土','左边沟回填',
                      '右边沟回填','左截沟填','左截沟挖','右截沟填','右截沟挖',
                      '挖台阶面积','左截沟挖','右截沟填','右截沟挖','挖台阶面积',]
        data['桩号']=data['桩号'].astype('str')
        return data
    except:
        print(f'{filename} 文件错误')




