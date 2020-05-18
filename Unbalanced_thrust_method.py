import math
from numpy import pi
"""
    功能：本函数输入相关土条参数(W_qi,Alpha_i,c_i,Phi_i,l_i,Alpha_i_1,E_i_1,F_s)，得到本块剩余下滑力E_i
        W_qi——第i个土条的重力与外加荷载之和（KN）；
        Alpha_i,Alpha_i_1——第i,i-1个土条底滑面的倾角(度);
        c_i,Phi_i——第i个土条的黏聚力（kPa）和内摩擦角(度);
        l_i——第i个土条的滑面长度（m）；
        E_i_1——第i-1个土条的下滑力
        F_s——安全系数；
    不平衡推力传递系数法
        1.计算公式只能用于计算Fs约等于1的边坡稳定安全系数，否则会造成大的误差
        2.因为分条这间不能承受拉力，所以任何土条的推力如果为负值，此Ei不再向下传递，对下一土条取E_i-1为0；
        3.推力从下往上算的时候累计传递推力之和都就是负数，否则不稳定 (自己总结)
        4.前后土条滑面角度差宜小于15度
        5.不平衡推力传递系数法视频介绍网址https://www.icourse163.org/learn/HHU-1003087004?tid=1206673210#/learn/content?type=detail&id=1211482076
    理正与路基规范公式不一致：理正及建筑地基基础设计规范采用简化公式
    
"""
def E_i(W_qi,Alpha_i,c_i,Phi_i,l_i,Alpha_i_1,E_i_1,F_s):
    Alpha_i = Alpha_i * 2 * pi / 360
    Phi_i = Phi_i * 2 * pi / 360
    Alpha_i_1 = Alpha_i_1 * 2 * pi / 360
    #1)路基设计规范中公式
    # Psi_i_1=math.cos(Alpha_i_1-Alpha_i)-math.tan(Phi_i)*math.sin(Alpha_i_1-Alpha_i)/F_s
    # E_i=W_qi*math.sin(Alpha_i)-(c_i*l_i+W_qi*math.cos(Alpha_i)*math.tan(Phi_i))/F_s+E_i_1*Psi_i_1
    # return E_i
    #2)理正公式及建筑地基基础设计规范简化公式
    if Alpha_i>90* 2 * pi / 360 :   #一般认为土条底滑面的倾角>90度为反向坡，此时滑块重力的分力及摩擦力为抗滑力不能乘以F_s
        F_s=1
    E_i=F_s*W_qi*math.sin(Alpha_i)+E_i_1*math.cos(Alpha_i_1-Alpha_i)-(W_qi*math.cos(Alpha_i)+E_i_1*math.sin(Alpha_i_1-Alpha_i))*math.tan(Phi_i)-c_i*l_i
    # 如Alpha_i为锐角A，反向坡时Alpha_i=360-A
    return E_i


W_qi=333.275+0
Alpha_i=23.962
c_i=10
Phi_i=30
l_i=4.515
Alpha_i_1=23.962
E_i_1=0
F_s=1.25
R=E_i(W_qi,Alpha_i,c_i,Phi_i,l_i,Alpha_i_1,E_i_1,F_s)
print(R)
# print(W_qi)
# print(math.cos(Alpha_i))
# print(W_qi*math.cos(Alpha_i))
# print(W_qi*math.cos(Alpha_i)*math.tan(Phi_i))
# print(math.cos(60*2*pi/360))


