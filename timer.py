from datetime import datetime


class Timer():

    def __init__(self,duration):
        self.start = 0
        self.duration = duration

    def remaining_Time(self):
        dt = datetime.now()
        t =  (dt.hour*60+dt.minute)*60+dt.second
        return self.start+self.duration-t

    def set_start(self,time):
        self.start = time

    @staticmethod
    def timelist_to_seconds(timelist):
        hours = (timelist[0]*10+timelist[1])
        minutes = (hours*60+timelist[2]*10+timelist[3])*60
        return minutes+timelist[4]*10+timelist[5]
