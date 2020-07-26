#======================调试用功能代码====================
# 1、单一腿坐标动作,num为的腿的编号
#    set_leg_CSYS(num,x,y,z)
#--------------------------------------------------------
# 2、所有腿坐标动作
#    set_legs_CSYS(x,y,z)
#--------------------------------------------------------
# 3、分别设置各腿高度
#    set_h(one,two,three,four)
#--------------------------------------------------------
# 4、整体高度动作，不会改变X与Z坐标值，动作受Kp_H控制速度
#    height(target)
#--------------------------------------------------------
# 5、航海角姿态控制
#    rotxzy(r,p,y)
import pctdog
import time
from pctdog.hardware.necir import NecIr   #红外控制
from pctdog.hardware.bm import necbm
from pctdog.hardware.bm import nec_cb

time.sleep(1)
pctdog.height(80)
time.sleep(1)
pctdog.rotxzy(0,-15,0)
pctdog.execute()
time.sleep(1)
pctdog.rotxzy(0,15,0)
pctdog.execute()
time.sleep(1)
pctdog.rotxzy(15,0,0)
pctdog.execute()
time.sleep(1)
pctdog.rotxzy(-15,0,0)
pctdog.execute()

nec1 = NecIr()
nec1.callback(nec_cb)
#前进24 后退82 左8 右90 *22 #13 1是69 2是70 3是71 4是68
#5是64 6是67 7是7 8是21 9是9 0是25 ok是28
while True:
    tNec = necbm()
    #4方向行走
    if tNec == 24:
        pctdog.trot(1,8)
    if tNec == 82:
        pctdog.trot(1,2)
    if tNec == 8:
        pctdog.trot(1,4)
    if tNec == 90:
        pctdog.trot(1,6)
    #蹲起动作
    if tNec == 22:
        pctdog.height(50)
        pctdog.set_legs_CSYS(0,50,0)
    if tNec == 13:
        pctdog.height(100)
        pctdog.set_legs_CSYS(0,100,0)
    #回复初始状态
    if tNec == 28:
        pctdog.set_legs_CSYS(0,80,0)

