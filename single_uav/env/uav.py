import numpy as np
import math
from robomaster import robot
import time
class UAV():
    def __init__(self,max_weight,fly_height):
        self.tl_drone = robot.Drone()
        self.tl_drone.initialize()

        self.tl_flight = self.tl_drone.flight
        self.cargo_buffer=[]
        self.speed=0
        self.sn_identity=0
        self.height=0
        self.fly_height=fly_height
        self.temperature=0
        self.max_weight=max_weight
        self.temp_weight=0
        self.battery=10
        self.cargo_index=0
        self.position=[0.0,0.0]
        self.start_position=[0.0,0.0]
    def get_angle(self,former_position,later_position,distance):
        delt_x=later_position[0]-former_position[0]
        delt_y=later_position[1]-former_position[1]
        right_or_left=1
        if delt_x!=0:
            right_or_left=delt_x/np.abs(delt_x)

        angle=math.degrees(math.acos(delt_y/distance))       
        angle=angle*right_or_left
        return angle
    def long_term_step(self,former_position,later_position,distance,cargo_index):
        
        # 计算要旋转的角度
        angle=self.get_angle(former_position,later_position,distance)
        
        # 起飞
        self.tl_flight.takeoff().wait_for_completed()

        self.tl_flight.rotate(angle=angle).wait_for_completed()

        # 前进
        self.tl_flight.forward(distance=distance).wait_for_completed()
        
        # 识别图像卡，校准位置
        self.correct(cargo_index)
        
        self.tl_flight.land().wait_for_completed()

        # led展示😊
        mled_smile1 = '000000000r0000r0r0r00r0r000000000000000000r00r00000rr00000000000'
        self.tl_drone.led.set_mled_graph(mled_smile1)
        time.sleep(3)
    
    def correct(self,cargo_index):
        
        mid='m'+str(cargo_index)
        
        self.tl_flight.mission_pad_on()

        # 飞行到挑战卡上方
        self.tl_flight.go(x=0, y=0, z=self.fly_height, speed=30, mid=mid).wait_for_completed()
        
        # led展示
        self.tl_drone.led.set_mled_char('r', cargo_index)
        time.sleep(0.5)
        return

        


    
    
    def sub_uav_info(self,info_dict):
        self.height=info_dict['height']
        self.temperature=info_dict['temperature']
        self.battery=info_dict['battery']
    # def take_off(height):  #直接调用SDK，起飞到指定高度
    #     return
    # def rotate():
    
        # return
    # def landing() #降落
    # def get_rotate_and_distance(cargo_info) #当无人机在货物点降落后，起飞前往下一个目标点
    # def get_cargo_info() #获取货物信息
    # def rotate() #选择无人机
    # def forward_backword() #前进或后退
    # def left_right() # 左右移动
    # def posture_calibration() #姿态校准
        