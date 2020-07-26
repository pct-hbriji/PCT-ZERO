#=============校准模式=============
calibration_mode=0
#=============机械结构=============
thigh=50        #大腿长(mm)
shank=70        #小腿长(mm)
shoulder=35.3   #肩部轴长(mm)
shoulderMAX=30  #肩部向下最大角度
shoulderMIN=-40 #肩部向上最大角度
bodylength=140  #整机长度
bodywidth=46    #整机宽度
#身体结构坐标
body_mat = [-bodylength/2,0,bodywidth/2,
            bodylength/2,0,bodywidth/2,
            -bodylength/2,0,-bodywidth/2,
            bodylength/2,0,-bodywidth/2]
#足端结构坐标
foot_mat = [-bodylength/2,0,bodywidth/2,
            bodylength/2,0,bodywidth/2,
            -bodylength/2,0,-bodywidth/2,
            bodylength/2,0,-bodywidth/2]
#=============PCA9685舵机控制板====
pcai2c = I2C(scl='Y9', sda='Y10', freq=100000)
#=============红外控制参数=========
tempNec = 0

#=============舵机初始位===========
#舵机与PCA9685接线：
#左前腿：小腿接0，大腿接1，肩部接2
#左后腿：小腿接4，大腿接5，肩部接6
#右前腿：小腿接8，大腿接9，肩部接10
#右后腿：小腿接12，大腿接13，肩部接14
init_leg = [82,97,95,       #左前腿：小腿舵机，大腿舵机，肩部舵机
            80,95,83,       #左后腿：小腿舵机，大腿舵机，肩部舵机
            83,90,92,       #右前腿：小腿舵机，大腿舵机，肩部舵机
            98,70,80]      #右后腿：小腿舵机，大腿舵机，肩部舵机   
#=============动作系数=============
Kp_H = 0.05      #动作延迟系数，0-1取值

#=============计算中参数===========
#参与计算的坐标
cac_CSYS = [0,0,0,
            0,0,0,
            0,0,0,
            0,0,0]
#初始姿态
int_CSYS = [0,60,shoulder,
            0,60,shoulder,
            0,60,-shoulder,
            0,60,-shoulder]
#计算用的舵机角度
cac_leg = [0,0,0,
           0,0,0,
           0,0,0,
           0,0,0]
#输出用舵机角度
out_leg = [0,0,0,
           0,0,0,
           0,0,0,
           0,0,0]
#坐标寄存器
check_CSYS = [0,0,0,
              0,0,0,
              0,0,0,
              0,0,0]
#坐标缓存器
log_CSYS = [0,0,0,
            0,0,0,
            0,0,0,
            0,0,0]
#姿态寄存器
check_trot = [0,0,0,0]

#========行走用参数================
walk_vector = [0,0,0,0]
Tstance = 0.5
Tswing = 0.5
S_se = [0,0]
Leg_lift_H = 20
walk_speed = 0.03
t = 0
