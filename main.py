from output.display_handler import Display_Handler
from output.sound_handler import Sound_Handler
from input_handler import Input_Handler
from datetime import datetime
from time import sleep

def main():
    outh = Display_Handler()
    inputh = Input_Handler(outh)
    timerlist = []
    flag = 0
    t = 0;

    while(timerlist == []):
        tempList = inputh.start()
        if(tempList != None):
            timerlist=tempList


    outh.set_first_line("Bereit")
    outh.set_second_line("")
    outh.write_display()
    while True:
        if outh.display.buttonPressed(outh.display.RIGHT):
            break

    dt = datetime.now()
    start = (dt.hour*60+dt.minute)*60+dt.second
    c = 0

    while True:
        timer = timerlist[c]
        outh.set_first_line("Timer %d" %(c+1))
        timer.set_start(start)
        rest = timer.remaining_Time()
        if timer == timerlist[-1] and rest <= 0:
            break
        if rest<=10.4 and flag==0:
            t = Sound_Handler(datetime.now())
            t.start()
            flag = 1
        if rest <= 0 :
            t.stop()
            flag = 0
            c = c+1
        outh.set_second_line(outh.seconds_to_time(rest))
        outh.write_display()
        cbefore = c
        c = inputh.switch_timer(c,len(timerlist)-1)
        cafter = c
        if cbefore != cafter:
            if type(t) != int:
                t.stop()
            flag = 0
        if c == -1:
            return
        sleep(0.2)

    outh.set_first_line("Fertig")
    outh.set_second_line("")
    outh.write_display()
    while True:
        if outh.display.buttonPressed(outh.display.SELECT):
            break

while True:
    main()
