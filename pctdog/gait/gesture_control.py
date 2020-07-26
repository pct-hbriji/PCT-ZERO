#设置单一腿坐标
def set_leg_CSYS(num,x,y,z):
    global cac_CSYS
    cac_CSYS[num*3] = x
    cac_CSYS[num*3+1] = y
    cac_CSYS[num*3+2] = z
    execute()
#所有腿同时调整坐标
def set_legs_CSYS(x,y,z):
    global cac_CSYS
    for i in range(4):
        cac_CSYS[i*3] = x
        cac_CSYS[i*3+1] = y
        if i < 2:
            cac_CSYS[i*3+2] = z
        else:
            cac_CSYS[i*3+2] = -z
    execute()
#分别设置各腿高度
def set_h(one,two,three,four):
    global cac_CSYS
    cac_CSYS[1] = one
    cac_CSYS[4] = two
    cac_CSYS[7] = three
    cac_CSYS[10] = four
    execute()
#整体高度调节函数，不会改变X与Z坐标
def height(target):
    global cac_CSYS
    while True:
        for i in range(4):
            if cac_CSYS[i*3+1] > target:
                cac_CSYS[i*3+1] = cac_CSYS[i*3+1] - (cac_CSYS[i*3+1] - target)*Kp_H
            elif cac_CSYS[i*3+1] < target:
                cac_CSYS[i*3+1] = cac_CSYS[i*3+1] + (target - cac_CSYS[i*3+1])*Kp_H
        if abs(cac_CSYS[1] - target) < 1 and abs(cac_CSYS[4] - target) < 1 and abs(cac_CSYS[7] - target) < 1 and abs(cac_CSYS[10] - target) < 1:
            break
        execute()

#航海角变换
def rotxzy(r,p,y):
    global cac_CSYS
    #角度转换为弧度
    r = r * pi / 180
    p = p * pi / 180
    y = y * pi / 180
    rot_mat = [cos(p)*cos(y) , -sin(p) , cos(p)*sin(y),
               cos(r)*sin(p)*cos(y) + sin(r)*sin(y) , cos(r)*cos(p) , cos(r)*sin(p)*sin(y) - sin(r)*cos(y),
               sin(r)*sin(p)*cos(y) - cos(r)*sin(y) , sin(r)*cos(p) , sin(r)*sin(p)*sin(y) + cos(r)*cos(y)]
    for i in range(4):
        cac_CSYS[i*3] = rot_mat[0]*(cac_CSYS[i*3] - body_mat[i*3]) + rot_mat[1]*(cac_CSYS[i*3+1] - body_mat[i*3+1]) + rot_mat[2]*(cac_CSYS[i*3+2] - body_mat[i*3+2]) + foot_mat[i*3]
        cac_CSYS[i*3+1] = rot_mat[3]*(cac_CSYS[i*3] - body_mat[i*3]) + rot_mat[4]*(cac_CSYS[i*3+1] - body_mat[i*3+1]) + rot_mat[5]*(cac_CSYS[i*3+2] - body_mat[i*3+2]) + foot_mat[i*3+1]
        cac_CSYS[i*3+2] = rot_mat[6]*(cac_CSYS[i*3] - body_mat[i*3]) + rot_mat[7]*(cac_CSYS[i*3+1] - body_mat[i*3+1]) + rot_mat[8]*(cac_CSYS[i*3+2] - body_mat[i*3+2]) + foot_mat[i*3+2]

#====舵机测试用=======
def test_def(num,x,y,z):
    global out_leg
    out_leg[num*3] = x
    out_leg[num*3+1] = y
    out_leg[num*3+2] = z
    servo_output()
    print_def()
