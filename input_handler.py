from timer import Timer
import sys
import os
import tty
import termios


class Input_Handler():

    def __init__(self,output_handler):
        self.ohandler = output_handler

    def readKey(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
        return  ch


    def readTime(self):
        timelist = [0,0,0,0,0,0]
        out = self.ohandler
        out.set_second_line(out.list_to_time(timelist))
        out.write_display()
        out.move_Cursor(out.cursor_col,out.cursor_row)
        out.blink()
        for i in range (0,6):
            if(out.cursor_col == 2 or out.cursor_col == 5):
                out.cursor_col+=1
            out.move_Cursor(out.cursor_col,out.cursor_row)
            while True:
                key = self.readKey()
                try:
                    key = int(key)
                    timelist[i] = key
                    break
                except:
                    if(ord(key) == 127):
                        return None

            out.set_second_line(out.list_to_time(timelist))
            out.write_display()
            out.cursor_col+=1
        out.unblink() 
        out.cursor_col=0
        out.cursor_row=1
        return Timer(Timer.timelist_to_seconds(timelist))

    def start(self):
        out = self.ohandler
        out.set_first_line("#Etappen: ")
        out.write_display()
        out.blink()
        number = ""
        while(True):
            out.set_second_line(number)
            out.write_display()
            key = self.readKey() 
            if(ord(key) == 13):
                break
            elif(ord(key) == 127):
                number = number[:-1]
            else:
                if(ord(key)>=48 and ord(key)<=57):
                    number+= str(key)
        if(number == ""):
            return
        number = int(number)
        return self.read_timer_list(number)

    def read_timer_list(self,number):
        timerlist = []
        timer = None
        while (len(timerlist) != number):
            self.ohandler.set_first_line("Timer %d" % (len(timerlist)+1))
            while(timer == None):
                timer = self.readTime()
                if(timer != None):
                    break
                else:
                    self.ohandler.cursor_row = 1
                    self.ohandler.cursor_col = 0
            if (timer!=None):
                timerlist.append(timer)
                timer = None
        return timerlist

    def switch_timer(self,c,max):
        lcd = self.ohandler.display
        if lcd.buttonPressed(lcd.UP):
            if c+1 > max:
                return c
            return c+1
        if lcd.buttonPressed(lcd.DOWN):
            if c-1 < 0:
                return c
            return c-1
        if lcd.buttonPressed(lcd.SELECT) :
            return -1
        return c





