from output.Adafruit_CharLCDPlate import  Adafruit_CharLCDPlate
import sys



class Display_Handler():

    def __init__(self):
        self.display = Adafruit_CharLCDPlate()
        self.display.begin(16,2)
        self.display.clear()
        self.first_line = ""
        self.second_line = ""
        self.cursor_row = 1
        self.cursor_col = 0

    def set_first_line(self,line):
        self.first_line = line

    def set_second_line(self,line):
        self.second_line = line

    def append_second_line(text):
        self.second_line+= text

    def write_display(self):
        self.display.clear()
        self.display.message("%s\n%s" %(self.first_line,self.second_line))

    def clear(self):
        self.display.clear()

    def blink(self):
        self.display.blink()

    def unblink(self):
        self.display.noBlink()

    def move_Cursor(self,col,row):
        self.display.setCursor(col,row)

    def list_to_time(self,list):
        return "%d%d:%d%d:%d%d" % (list[0],list[1],list[2],list[3],list[4],\
                list[5])

    def seconds_to_time(self,seconds):
        m,s = divmod(seconds,60)
        h,m = divmod(m,60)
        return "%02d:%02d:%02d" % (h,m,s)

    def list_to_number(self,list):
        number = 0
        l = len(list)
        for elem in list:
            number+=elem*(10**l)
            l-=1
        print number

