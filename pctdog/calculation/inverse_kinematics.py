#======坐标逆解======
#(num*3)  为小腿
#(num*3+1)为大腿
#(num*3+2)为肩部
def inverse_solution():
    global cac_leg
    global cac_CSYS
    for num in range(4):
        #大小腿平面的相对y，平方
        ydef = cac_CSYS[num*3+1]**2 + (cac_CSYS[num*3+2])**2 - shoulder**2
        #大小腿平面的对角线d，平方
        ddef = shoulder**2 + ydef
        #大腿轴到足端距离d2计算，平方
        d2def = ydef + cac_CSYS[num*3]**2
        #小腿角度
        cac_leg[num*3] = acos((thigh**2 + shank**2 - d2def)/(2*thigh*shank))

        #肩部舵机角度
        if num < 2:
            if cac_CSYS[num*3+2] > shoulder:
                cac_leg[num*3+2] = pi/2 + atan(ydef**0.5/shoulder) - atan(abs(cac_CSYS[num*3+1])/abs(cac_CSYS[num*3+2]))
            elif cac_CSYS[num*3+2] == shoulder:
                cac_leg[num*3+2] = pi/2
            elif cac_CSYS[num*3+2] < shoulder and cac_CSYS[num*3+2] > 0:
                cac_leg[num*3+2] = pi/2 + atan(ydef**0.5/shoulder) - atan(abs(cac_CSYS[num*3+1])/abs(cac_CSYS[num*3+2]))
            elif cac_CSYS[num*3+2] == 0:
                cac_leg[num*3+2] = atan(ydef**0.5/shoulder)
            elif cac_CSYS[num*3+2] < 0:
                cac_leg[num*3+2] = atan(ydef**0.5/shoulder) + atan(abs(cac_CSYS[num*3+1])/abs(cac_CSYS[num*3+2])) - pi/2
        else:
            if cac_CSYS[num*3+2] > shoulder and cac_CSYS[num*3+2] < 0:
                cac_leg[num*3+2] = pi -  atan(ydef**0.5/shoulder) + atan(abs(cac_CSYS[num*3+1])/abs(cac_CSYS[num*3+2]))
            elif cac_CSYS[num*3+2] == -shoulder:
                cac_leg[num*3+2] = pi/2
            elif cac_CSYS[num*3+2] < shoulder:
                cac_leg[num*3+2] = pi/2 - atan(ydef**0.5/shoulder) + atan(abs(cac_CSYS[num*3+1])/abs(cac_CSYS[num*3+2]))
            elif cac_CSYS[num*3+2] == 0:
                cac_leg[num*3+2] = pi - atan(ydef**0.5/shoulder)
            elif cac_CSYS[num*3+2] > 0:
                cac_leg[num*3+2] = pi - atan(ydef**0.5/shoulder) - atan(abs(cac_CSYS[num*3+1])/abs(cac_CSYS[num*3+2])) + pi/2

        #辅助角计算
        aux1 = acos((d2def + thigh**2 - shank**2)/(2*(d2def**0.5)*thigh))
        #大腿角度计算
        if cac_CSYS[num*3]>0:
                cac_leg[num*3+1] = pi - (pi/2 - abs(atan(cac_CSYS[num*3]/(ydef**0.5))) - aux1)
        elif cac_CSYS[num*3]==0:
                cac_leg[num*3+1] = pi/2 + aux1
        elif cac_CSYS[num*3]<0:
                cac_leg[num*3+1] = pi - (pi/2 + abs(atan(cac_CSYS[num*3]/(ydef**0.5))) - aux1)
    #弧度与角度进行转换
    for i in range(len(cac_leg)):
        cac_leg[i] = 180 * cac_leg[i] / pi

#====角度极限计算====
def angle_limit():
    global out_leg
    global cac_leg
    
    for i in range(4):
        if i ==0 or i == 1:
            out_leg[i*3] = 180 - init_leg[i*3] + 90 - cac_leg[i*3]
            out_leg[i*3+1] = init_leg[i*3+1] - 90 + cac_leg[i*3+1] + 17.46
            out_leg[i*3+2] = init_leg[i*3+2] - 90 + cac_leg[i*3+2]
        elif i == 2 or i == 3:
            out_leg[i*3] = init_leg[i*3] - 90 + cac_leg[i*3] - 8.73
            out_leg[i*3+1] = 180 - init_leg[i*3+1] + 90 - cac_leg[i*3+1] - 17.46
            out_leg[i*3+2] = init_leg[i*3+2] - 90 + cac_leg[i*3+2]
    #对肩部舵机进行角度预处理
    '''
    for i in range(4):
        if cac_leg[i*3+2] < shoulderMIN:cac_leg[i*3+2] = shoulderMIN
        if cac_leg[i*3+2] > shoulderMAX:cac_leg[i*3+2] = shoulderMAX
    '''
    #输出角度取整
    for i in range(len(out_leg)):
        out_leg[i] = int(out_leg[i])
    for i in range(len(out_leg)):
        if out_leg[i] > 179:out_leg[i]=179
        if out_leg[i] < 1:out_leg[i]=1


#======舵机输出======
def servo_output():
    global out_leg
    #调试模式为1
    if calibration_mode == 0:
        for i in range(len(out_leg)):
            servos.position(i, degrees = out_leg[i])
    else:
        for i in range(len(init_leg)):
            servos.position(i, degrees = init_leg[i])
	print("调试完成！")

#=====执行命令打包====
def execute():
    inverse_solution()
    angle_limit()
    servo_output()
    #print_def()

#====寄存矩阵清空=====
def reset_check():
    walk_vector = [0,0,0,0]
    S_se = [0,0]
    check_trot = [0,0,0,0]
    check_CSYS = [0,0,0,0]
    cac_CSYS = int_CSYS

#====打印测试=========
def print_def():
    for i in range(4):
        print("编号：",i+1)
        print("X:",cac_CSYS[i*3],"  Y:",cac_CSYS[i*3+1],"  Z:",cac_CSYS[i*3+2])
        print("调整前小腿:",cac_leg[i*3],"  大腿:",cac_leg[i*3+1],"  肩部:",cac_leg[i*3+2])
        print("输出的小腿:",out_leg[i*3],"  大腿:",out_leg[i*3+1],"  肩部:",out_leg[i*3+2])
