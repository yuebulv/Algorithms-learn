import sys
sys.path.append(r'F:\git\Algorithms-learn\inf_slop')
sys.path.append(r'F:\git\Algorithms-learn\Unbalanced_thrust_method')
import inf_slop
import math
import Unbalanced_thrust_method
from numpy import pi
def analyse_slop(key,tf_filename,d3r_filename,hdm_filename):
    res=[]
    for side_LOR in [0,1]:  #0代表左侧，1代表右侧
        xy_slop=inf_slop.infofslop(key,side_LOR,tf_filename,d3r_filename,hdm_filename)
        #要取得路基左宽右宽判断填挖
        r=19;i=1;dare=[];angle=[];li=[];ci=[];phi=[];W_qi=[];F_s=1.25
        for content in xy_slop[0][1:]: #根据边坡信息得到，计算推力所需参数
            h2=xy_slop[1][i]-xy_slop[2][i]
            h1=xy_slop[1][i-1]-xy_slop[2][i-1]
            dx=xy_slop[0][i]-xy_slop[0][i-1]
            dare.append((h2+h1)*dx/2)
            W_qi.append(dare[i-1]*r)
            tem =math.atan((xy_slop[2][i] - xy_slop[2][i - 1]) / (dx))
            li.append(dx/math.cos(tem))
            angle.append(tem*360/2/pi)
            ci.append(10)
            phi.append(30)
            i+=1
        i=0;thrust=[]
        for content in W_qi:
            try:
                thrust.append(Unbalanced_thrust_method.E_i(W_qi[i],angle[i],ci[i],phi[i],li[i],angle[i-1],thrust[i-1],F_s))
                i += 1
            except IndexError:
                thrust.append(Unbalanced_thrust_method.E_i(W_qi[i], angle[i], ci[i], phi[i], li[i], angle[i - 1], 0, F_s))
        res.append(xy_slop)
        res.append(thrust)
    return res

key='6255.031'
# key='6260.000'
tf_filename = r'e:\A.tf'
d3r_filename = r'e:\a\A.3dr'
hdm_filename = r'e:\a\A.hdm'
s=analyse_slop(key,tf_filename,d3r_filename,hdm_filename)
i=0
for content in s:
    print(s[i])
    i+=1
