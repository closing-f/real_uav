
class Cargo:
    def __init__(self,position,wait_time):
        self.postion=position
        self.wait_time=wait_time
        self.whether_got=False
    
    def increase_wait_time(self,time):
        self.wait_time+=time
    
    def set_whether_got(self,got):
        self.whether_got=got
    