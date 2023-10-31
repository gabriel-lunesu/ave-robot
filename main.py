from hub import light_matrix
from motor import velocity
import runloop
import motor_pair
import color_sensor
import math
import time
from hub import port
import color


    


async def moveForward(): # function to move forward
    motor_pair.pair(motor_pair.PAIR_1,port.C,port.D)


    motor_pair.move(motor_pair.PAIR_1, 0)


async def moveLeft(): # function to turn a bit left
    motor_pair.pair(motor_pair.PAIR_1,port.C,port.D)


    motor_pair.move_tank_for_time(motor_pair.PAIR_1, 0, 200, 700)

async def moveRight(): # function to turn a bit right
    motor_pair.pair(motor_pair.PAIR_1,port.C,port.D)


    motor_pair.move_tank_for_time(motor_pair.PAIR_1, 200, 0, 700)

async def detectRed(): #function to detect red color by using color sensor 
    color_sensor.color(port.F)

    while color_sensor.color(port.F) is 9:
        
        light_matrix.write("RED")

async def motorFreeze(): #motor stops for 5 seconds
    motor_pair.pair(motor_pair.PAIR_1,port.C,port.D)
        
    motor_pair.stop(motor_pair.PAIR_1)

    time.sleep_ms(5000)    

async def main():
    runloop.run(moveLeft())
    runloop.run(moveRight())
    runloop.run(motorFreeze())
    runloop.run(moveForward())  

runloop.run(main())
