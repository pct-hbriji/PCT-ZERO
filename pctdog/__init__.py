from math import *        #导入全部数学函数
from machine import I2C   #与pca9685连接要用I2C
from pyb import UART      #板载串口
from pyb import Pin       #板载引脚
import time               #时间处理模块
#import _thread           #多线程模块

#==============版本信息==================#
ver="V0.72 BETA 20200718"

#打印版本信息
print("       $$$$$$$$$$   $$$$$$$   $$$$$$$$$$       ")
print("      $========$=  $======/      $=====/       ")
print("     $=/      $=  $=/           $=/            ")
print("    $=/      $=  $=/           $=/             ")
print("   $$$$$$$$$$=  $=/           $=/              ")
print("  $==========  $=/           $=/               ")
print(" $=/          $=/           $=/                ")
print("$=/          $$$$$$$$$     $=/                 ")
print("=/          ========/     ==/                  ")
print("PCT-DOG "+ver+"  MAKER：黑白日记")
print("--------------------------------------------------")
print("加载程序...")
Init_File_List=[".//pctdog//config.py",
                ".//pctdog//hardware//pca9685.py",
                ".//pctdog//hardware//servo.py",
                ".//pctdog//hardware//necir.py",
                ".//pctdog//hardware//bm.py",
                ".//pctdog//calculation//inverse_kinematics.py",
                ".//pctdog//calculation//forward_kinematics.py",
                ".//pctdog//gait//trot.py",
                ".//pctdog//gait//gesture_control.py",
                ".//pctdog//gait//imu.py"]

#调试使用
jd='\r %2d%% [%s%s]'
x=0
for i in Init_File_List:
    exec(open(i).read())
    x = x+1
    a = '■'*(x+1)
    b = '□'*(len(Init_File_List)-x)
    c = (x/len(Init_File_List))*100
    print(jd % (c,a,b),end='')

print("程序加载完成...")

#开机初始化动作
positive_solution()
