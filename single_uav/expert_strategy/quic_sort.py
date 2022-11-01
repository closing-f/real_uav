class quic_sort:
    def __init__(self,):
        self.index_list=None
        self.arr = None
    
    def partition(self,low,high): 
        i = ( low-1 )         # 最小元素索引
        pivot = self.arr[high]     
    
        for j in range(low , high): 
    
            # 当前元素小于或等于 pivot 
            if self.arr[j] <= pivot: 
            
                i = i+1 
                self.arr[i],self.arr[j] = self.arr[j],self.arr[i] 
                self.index_list[i],self.index_list[j]= self.index_list[j],self.index_list[i] 
        self.arr[i+1],self.arr[high] = self.arr[high],self.arr[i+1] 
        self.index_list[i+1],self.index_list[high] = self.index_list[high],self.index_list[i+1] 
        return ( i+1 ) 
  
 
# self.arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引
  
# 快速排序函数
    def quickSort(self,low,high): 
        if low < high: 
    
            pi = self.partition(self.arr,low,high) 
    
            self.quickSort(self.arr, low, pi-1) 
            self.quickSort(self.arr, pi+1, high) 
    
    def start(self,arr,index_list):
        self.index_list=index_list
        self.arr = arr
        # self.arr = [10, 7, 8, 9, 1, 5] 
        n = len(self.arr) 
        self.quickSort(self.arr,0,n-1) 
        return self.arr, self.index_list