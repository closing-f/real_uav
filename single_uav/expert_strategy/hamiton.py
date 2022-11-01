#用dfs 计算最短Hamiton回路
import numpy as np
class Hamiton:
    def __init__(self,maxn,distance,seq):
        self.maxn = maxn
        self.distance=distance # n个点，m条边，dis[i][j]是i点到j点的距离
        self.vis=np.zeros((self.maxn,)) #标记每个点是否到过
        self.best_seq=np.zeros((self.maxn,))
        self.best_ans=0 # 最短距离
        
        self.node=seq # node 路径结点
        self.len_seq=len(self.node)
        self.seq=np.zeros((self.len_seq,)) # seq当前路径结点序列，best_seq最短路径的结点序列
        
    def dfs(self, s, now_point, len, sum): # 从s号点出发，走过了len个结点，当前总长为sum
        if ( sum > self.best_ans ):#剪枝：已经不可能找到更短的了
            return
        
        if ( len == self.len_seq ): #遍历完所有结点
            if ( sum + self.distance[now_point][s] < self.best_ans ): # 更新最短路径
                for i in range(self.len_seq):
                    self.best_seq[i] = self.seq[i] 
                
                self.best_ans = sum + self.distance[now_point][s]

            return 
        
        for i in range(self.maxn): # 枚举当前点的所有出边，走第i条出边
            
            # self.vis[now_point] = 1
            
            if self.vis[i] == 0:
                self.vis[i]= 1
                self.seq[len]=i
                self.dfs( s , i , len+1 , sum+self.distance[now_point][i] )
                self.vis[i] = 0
    
    def start(self,):
        
        for i in range(self.maxn):
            self.vis[i]=-1
        for i in range(self.len_seq):
            self.vis[self.node[i]]=0
        
        self.vis[self.node[0]] = 1
        
        self.seq[0]=self.node[0]
        
        self.dfs(self.seq[0],self.seq[0],1,0)
        
        return self.best_seq
    
