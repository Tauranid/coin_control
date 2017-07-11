#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from threading import Timer
import subprocess

#CONSTANTS
switch_pin = 7 # the interrupt gpio pin
screen_timeout = 5*60 # screen timeout in seconds

#TECHNICAL CONSTANTS (Don't change once working as intended)
switch_debounce = 0.5 # switch debounce time in seconds
debounce_flag = 0

#And theres this variable which totally should go to the bottom of the script...
total_passes = 0 # number of passes for the timer


def timer_debounce_finish():
    global debounce_flag
    debounce_flag = 0

def insert_coin(pin):
    global total_passes
    global debounce_flag
    
    if (debounce_flag == 0):        
        if (total_passes <= 0):
            print("turn on screen now")
            subprocess.Popen(['/home/pi/coin_control/screen_on.sh'])
            screen_timer = Timer(screen_timeout + 3, timer_screen_finish)
            screen_timer.start()

        debounce_timer = Timer(switch_debounce, timer_debounce_finish)
	debounce_flag = 1
        total_passes += 1
        debounce_timer.start()
        print("increase passes to " + str(total_passes))

def timer_screen_finish():
    global total_passes
    total_passes -= 1
    print("decrease passes to " + str(total_passes))
    if total_passes <= 0:
        print("turn screen off again")
        subprocess.Popen(['/home/pi/coin_control/screen_off.sh'])
    else:
        screen_timer = Timer(screen_timeout, timer_screen_finish)
	screen_timer.start()


def loop():
	while True:
		time.sleep(1)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(switch_pin, GPIO.IN)

    GPIO.add_event_detect(switch_pin, GPIO.RISING, callback=insert_coin)

    loop()
