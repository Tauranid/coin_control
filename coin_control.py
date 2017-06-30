import RPi.GPIO as GPIO
import time
from threading import Timer

switch_pin = 7 # the interrupt gpio pin
screen_timeout = 10 # screen timeout in minutes
total_passes = 0 # number of passes for the timer

def insert_coin(pin):
    global total_passes
    if (total_passes <= 0):
        print("turn on screen now")
        timer.start()
    else:
        pass
    total_passes += 1

def timer_finish():
    total_passes -= 1
    if total_passes <= 0:
        print("turn screen off again")
    else:
        pass


def loop():
	while (1):
		time.sleep(1)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch_pin, GPIO.IN)

GPIO.add_event_detect(switch_pin, GPIO.RISING, callback=insert_coin)
timer = Timer(screen_timeout*60.0, timer_finish)

loop()
