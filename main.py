# This is the main script for the LEGO robot for this school project.
# DEVS; 
# Gabriel Lunesu, Yasin Leclaire, Tom Creemers, ...
# Start [15 sep 2023]
# Last edited [6 oct 2023]
# Last important change: ""(KEEP EMPTY IF NOTHING TO NOTE)

from hub import light_matrix
import runloop
import motor_pair
import color_sensor
import math
import time
from hub import port
import color

async def main():
    
    await light_matrix.write("Hi!")
    motor_pair.pair(motor_pair.PAIR_1,port.C,port.D)
    start_time = time.ticks_ms()
    while time.ticks_ms() - start_time < 50000:
        motor_pair.move(motor_pair.PAIR_1,(math.floor(-3/5)*color_sensor.reflection(port.F)+30),velocity=170)
       
        if color_sensor.color(port.F) is color.RED:
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=0)
            
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())