#num为步数，ori为方向控制
#ori取值采用数字键盘方向设定
#====================================
#       8前进
#4左转    +    6右转
#       2后退
#====================================
def trot(num,ori):
    global walk_vector,cac_CSYS,check_CSYS,check_trot,S_se,log_CSYS
    global t,pitchangle
    for i in range(4):
        cac_CSYS[i*3] = 0
        cac_CSYS[i*3+1] = 80
        cac_CSYS[i*3+2] = 0
    log_CSYS = cac_CSYS
    for k in range(4):
        print("历史坐标初始化： x：",log_CSYS[k*3]," y:",log_CSYS[k*3+1]," z:",log_CSYS[k*3+2])
    check_CSYS = cac_CSYS
    #处理方向变量
    if ori == 8:
        walk_vector = [1,1,1,1]     #向前行走
        S_se = [-20,20]
    elif ori == 2:
        walk_vector = [-1,-1,-1,-1] #向后行走
        S_se = [-20,20]
    elif ori == 4:
        walk_vector = [-1,-1,1,1]   #向左转
        S_se = [-20,20]
    elif ori == 6:
        walk_vector = [1,1,-1,-1]   #向右转
        S_se = [-20,20]
    for i in range(abs(num)):
        while True:
            if t >= Tswing + Tstance:
                t = 0
                break
            else:
                t = t + walk_speed
                if t <= Tswing:
                    sigma = 2*pi*t/Tswing
                    check_trot = [1,0,0,1]
                if t > Tswing and t < Tswing + Tstance:
                    sigma = 2*pi*(t - (Tswing + Tstance)*Tstance)/Tstance
                    check_trot = [0,1,1,0]

                for k in range(4):

                    check_CSYS[k*3+1] = Leg_lift_H * (1-cos(sigma))/2

                    cac_CSYS[k*3+1] = 80 - check_trot[k]*check_CSYS[k*3+1]

                    if check_trot[k] == 1:
                        cac_CSYS[k*3] = walk_vector[k]*((S_se[0] - S_se[1])*((sigma - sin(sigma))/(2*pi)) + S_se[1])
                    else:
                        cac_CSYS[k*3] = walk_vector[k]*((S_se[1] - S_se[0])*((sigma - sin(sigma))/(2*pi)) + S_se[0])

            print("步行前参数：")
            for k in range(4):
                print(cac_CSYS[k*3]," ",cac_CSYS[k*3+1]," ",cac_CSYS[k*3+2])
            #pitch_angle(5)
            execute()
    reset_check()
    #execute()
