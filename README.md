# PCT-ZERO

## 模块化MicroPython舵机控制核心

## 介绍
这是一个多元模块化开源项目
主旨：利用一个核心控制单元，控制多种不同种类的机器人单元

### 目前开发进度
- [x] 已完成项目
  - [x] 核心模块
  - [x] 12自由度四足机器人
- [ ] 未完成项目
  - [ ] 核心模块常用功能库
  - [ ] 8自由度四足机器人模块
  - [ ] 并联腿四足机器人模块
  - [ ] 四足机器人表情等娱乐功能库
  - [ ] 3自由度机械臂模块
  - [ ] 5自由度机械臂模块
  - [ ] 四轮小车模块
 
目前该项目还是草创阶段，后续会不断丰富起来

### 使用依赖
1. PYBoard STM32F405 开发板（MicroPython）
2. PCA9685舵机驱动板
3. XL4005 或其它 5A DC-DC 5-32V电源模块
4. 2S航模电池
5. KCD1-101小船型开关 或其它替代
6. MG90S舵机若干
7. 17键迷你红外无限遥控器模块（非必须）
8. 3D打印件（自行打印或委托打印）

### 目录结构描述

源代码
├── main // 主程序
├── pctdog // 12自由度四足机器人库
│ ├── __init__.py // 初始化文件
│ ├── config.py // 参数定义文件
│ ├── calculation
│ │ ├── forward_kinematics.py // 开机动作初始化
│ │ └── inverse_kinematics.py // 坐标逆解
│ ├── contorl
│ │ ├── nec_control.py // 红外线控制程序
│ │ └── nec_key.py // 红外线键值枚举表
│ ├── gait
│ │ ├── gait.py // 步行姿态
│ │ ├── gesture_control.py // 姿态控制
│ │ ├── trot.py // 跑步
│ │ └── walk.py // 漫步
│ └── hardware
│ ├── bm.py // 测试环境
│ ├── necir.py // 红外遥控器驱动
│ ├── pca9685.py // PCA9685舵机驱动板驱动
│ └── servo.py // 舵机控制驱动
├── Readme.md // help
└── LICENSE // 开源声明

####V0.72 版本内容更新

1. set_leg_CSYS(num, x, y, z):