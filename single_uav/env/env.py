
from robomaster import drone
from uav import UAV
from cargo import Cargo
import numpy as np
class Env():
    def __init__(self,config):
        self.num_uav=config.num_uav
        self.num_cargo=config.num_cargo
        self.fly_heights=config.fly_heights
        self.uav_max_weight=config.max_weight
        self.UAVs=[UAV(self.uav_max_weight,self.fly_heights[i]) for i in range(self.num_uav)]
        cargo_position=np.zeros((self.num_cargo,2))
        cargo_wait_time=np.zeros((self.num_cargo,))
        self.Cargoes=[Cargo(cargo_position[i],cargo_wait_time[i]) for i in range(self.num_cargo)]
        self.distance_matrix=None
    def select_step():
        return
    def get_cargo_wait_time(self,):

        return [self.Cargoes[i].wait_time for i in range(self.num_cargo) if self.Cargoes[i].whether_got==False]
    def get_cargo_index(self,):
        return [i for i in range(self.num_cargo) if self.Cargoes[i].whether_got==False]
    def get_cargo_whether_got(self,):
        return [self.Cargoes[i].whether_got for i in range(self.num_cargo)]
    def get_cargo_position(self,):
        return [self.Cargoes[i].postion for i in range(self.num_cargo)]
    def get_cargo_distance(self,):
        distance=np.zeros((self.num_cargo,self.num_cargo))
        for i in range(self.num_cargo):
            for j in range(self.num_cargo):
                postion_i=self.Cargoes[i].postion
                postion_j=self.Cargoes[j].postion
                distance[i][j]=self.get_points_distance(postion_i[0],postion_i[1],postion_j[0],postion_j[1])
        return distance 
    def set_cargo_whether_got(self,cargo_index,whether_got):
        self.Cargoes[cargo_index].set_whether_got(whether_got)

    def get_points_distance(x1,x2,y1,y2):
        return np.sqrt(np.power((x1-x2),2)+np.power((y1-y2),2))
