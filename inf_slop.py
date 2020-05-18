import sys
sys.path.append(r'F:\git\Algorithms-learn\getdata_hdm')
sys.path.append(r'F:\git\Algorithms-learn\getdata_tf')
import getdata_hdm
import getdata_tf
'''
    功能：已知(key,side_LOR,tf_filename,d3r_filename,hdm_filename)，输出[list1,list2,list3]范围内设计线，地面线
    key：桩号
    side_LOR：路基左侧为0，右侧为1
    tf_filename：tf文件绝对路径
    d3r_filename：3dr文件绝对路径
    hdm_filename：hdm文件绝对路径
    list1：x轴
    list2：路基设计线Y轴
    list3：地面线Y轴
    例句
    import sys
    sys.path.append(r'F:\git\Algorithms-learn\inf_slop')
    import inf_slop
    side_LOR=1  #0代表左侧，1代表右侧
    key='6255.031'
    # key='6260.000'
    tf_filename = r'e:\A.tf'
    d3r_filename = r'e:\a\A.3dr'
    hdm_filename = r'e:\a\A.hdm'
    s=inf_slop.infofslop(key,side_LOR,tf_filename,d3r_filename,hdm_filename)
    print(s[0])
    print(s[1])
    print(s[2])

'''
def infofslop(key,side_LOR,tf_filename,d3r_filename,hdm_filename):
    # side_LOR=0  #0代表左侧，1代表右侧
    # key='6255.031'
    #获得中桩填挖-----------------------------------------------------------------------------
    try:
        # tf_filename = r'e:\A.tf'
        Df_tf=getdata_tf.tf(tf_filename)#[['桩号','中桩填挖']] #中桩填挖  路基左宽 路基右宽
        condition=(Df_tf['桩号']==key)
        difheight_key=Df_tf[condition][['桩号','中桩填挖']].values[0][1]
    except IndexError:
        print(f'{tf_filename} 这个文件不存在桩号{key}')

    #获得3dr-----------------------------------------------------------------------------
    # d3r_filename = r'e:\a\A.3dr'
    D_3dr=getdata_hdm.hdm(d3r_filename)
    d3rvalue_xy=D_3dr[key]
    d3rvalue_x=d3rvalue_xy[side_LOR][1::2]
    d3rvalue_y=d3rvalue_xy[side_LOR][2::2]
    i=0
    for hvalue in d3rvalue_x:
        d3rvalue_x[i] = round(float(d3rvalue_x[i]),4)
        i+=1
    border_x=d3rvalue_x[(i-1)]
    i=0
    for hvalue in d3rvalue_y:
        d3rvalue_y[i] = round(float(d3rvalue_y[i]),4)
        i+=1
    desheight=float(d3rvalue_y[0])

    #获得hdm-----------------------------------------------------------------------------
    # hdm_filename = r'e:\a\A.hdm'
    D_hdm=getdata_hdm.hdm(hdm_filename)
    hdmvalue_xy=D_hdm[key]
    hdmvalue_x=hdmvalue_xy[side_LOR][1::2]
    hdmvalue_y=hdmvalue_xy[side_LOR][2::2]
    sign=[-1,1]
    hsum=0
    i=0
    for hvalue in hdmvalue_x: #hdm数据转为距中桩的距离及高程
        hsum += float(hvalue)
        hdmvalue_x[i] = round(hsum,4)*sign[side_LOR]
        i+=1
    newx=hdmvalue_x[:] # 复制
    newx.insert(0,border_x)
    newx.sort()
    location=newx.index(border_x)
    if side_LOR==0: #只保留路基范围hdm_x数据
        location=len(hdmvalue_x)-location+1
        hdmvalue_x=hdmvalue_x[:(location)]
    else:
        if side_LOR==1:
            hdmvalue_x = hdmvalue_x[:(location)]
    hsum=0
    i=0
    hdmvalue_y=hdmvalue_y[:(location)]  #只保留路基范围hdm_y数据
    for hvalue in hdmvalue_y:
        hsum += float(hvalue)
        hdmvalue_y[i] = round(hsum+desheight-difheight_key,4)
        i+=1
    hdmvalue_x.insert(0,0)
    hdmvalue_y.insert(0,desheight-difheight_key)

    #hdm范围小于3dr范围时，自动延长hdm范围
    location=len(hdmvalue_x)-1
    if abs(hdmvalue_x[location])<abs(border_x):
        hdmvalue_x.append(border_x)
        try:
            height = (hdmvalue_y[location] - hdmvalue_y[location - 1]) / \
                     (hdmvalue_x[location] - hdmvalue_x[location - 1]) * \
                     (border_x - hdmvalue_x[location]) + hdmvalue_y[location]
            hdmvalue_y.append(round(height, 4))
        except:
            hdmvalue_y.append(hdmvalue_y[location])

    #获得newx，new3dr_y-----------------------------------------------------------------------------
    newx=[]
    newx=hdmvalue_x+d3rvalue_x # 存储3dr数据距在桩的水平距离
    newx.sort()
    list2=[]
    [list2.append(i) for i in newx if not i in list2] #删除重复元素
    newx=list2[:]
    new3dr_y=[] # 用于获取newx对应3dr的高程值
    for i in list2:
        if abs(i)>abs(d3rvalue_x[len(d3rvalue_x)-1]) or abs(i)<abs(d3rvalue_x[0]):
            newx.remove(i)
            continue
        else:
            try:
                location=d3rvalue_x.index(i)
                new3dr_y.append(d3rvalue_y[location])
            except ValueError:
                new3drx=d3rvalue_x[:]
                new3drx.insert(0,i)
                if side_LOR==0:
                    new3drx.sort(reverse=True)
                else:
                    new3drx.sort()
                location=new3drx.index(i)
                height=(d3rvalue_y[location]-d3rvalue_y[location-1])/\
                       (d3rvalue_x[location]-d3rvalue_x[location-1])*\
                       (i-d3rvalue_x[location-1])+d3rvalue_y[location-1]
                new3dr_y.append(round(height,4))
    del list2
    # 获得newx，newhdm_y-----------------------------------------------------------------------------
    newhdm_y=[] # 用于获取newx对应3dr的高程值
    for i in newx:
        if abs(i)>abs(hdmvalue_x[len(hdmvalue_x)-1]) or abs(i)<abs(hdmvalue_x[0]):
            #如果hdm范围小于3dr范围，则自动延长hdm线
            continue
        else:
            try:
                location=hdmvalue_x.index(i)
                newhdm_y.append(hdmvalue_y[location])
            except ValueError:
                new3drx=hdmvalue_x[:]
                new3drx.insert(0,i)
                if side_LOR==0:
                    new3drx.sort(reverse=True)
                else:
                    new3drx.sort()
                location=new3drx.index(i)
                height=(hdmvalue_y[location]-hdmvalue_y[location-1])/\
                       (hdmvalue_x[location]-hdmvalue_x[location-1])*\
                       (i-hdmvalue_x[location-1])+hdmvalue_y[location-1]
                newhdm_y.append(round(height,4))
    res=[]
    res.append(newx)
    res.append(new3dr_y)
    res.append(newhdm_y)

    return res





