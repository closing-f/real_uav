import imp
import numpy as np
import math
from env.env import Env
import argparse  # 1、导入argpase包
from env.uav import UAV
import quic_sort
from single_uav.expert_strategy.hamiton import Hamiton
def parse_args():
    parse = argparse.ArgumentParser(description='real uav')  # 2、创建参数对象
    parse.add_argument('num_uav', type=int, default=1 ,help='number of UAVs')
    parse.add_argument('num_cargo', type=int, default=4 ,help='number of cargoes') 
    parse.add_argument('fly_heights', type=list, default=[50,50,50,50] ,help='飞行高度')
    parse.add_argument('max_weight',type=int, default=4, help='飞行负载')
    args = parse.parse_args()
    return args

def time_sensitive_greedy_select(index_list,cargo_wait_time,k):
    
    cargo_total_num=len(index_list)
    cargo_taken_num=np.max=(cargo_total_num,k)
    quicsort=quic_sort()
    index_after_sort=quicsort.start(cargo_wait_time,index_list)
    return index_after_sort[cargo_total_num-cargo_taken_num:]

args = parse_args()

num_uav=args.num_uav
num_cargo=args.num_cargo
env=Env(args)
uav=UAV(args.max_weight,args.fly_heights[0])

cargo_index=env.get_cargo_index()
cargo_distance=env.get_cargo_distance()
cargo_wait_time=env.get_cargo_wait_time()
cargo_position=env.get_cargo_position()

# 只考虑货物等待时间
seq=time_sensitive_greedy_select(cargo_index,cargo_wait_time,k=3)
seq.insert(0,0)

# 利用dfs计算从原点开始经过各选择货物点后回到原点的路径
hamiton=Hamiton(num_cargo,cargo_distance,seq)
best_seq=hamiton.start()
best_seq.append(0)

# [0,2,4,3,0]

for i in range(1,len(best_seq)):
    distance=cargo_distance[best_seq[i]][best_seq[i-1]]
    UAV.long_term_step(cargo_position[i-1],cargo_position[i],distance,best_seq[i])


    








