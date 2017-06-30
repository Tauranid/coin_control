import RPi.GPIO as GPIO
import time

switch_pin = 7 # the interrupt gpio pin
screen_timeout = 10 # screen timeout in minutes



GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch_pin, GPIO.IN)

def interrupt_callback(pin):
	print "turn off screen now"
	time.sleep(5)
	print "turn screen on again"

def loop():
	while (1):
		time.sleep(1)

GPIO.add_event_detect(switch_pin, GPIO.RISING, callback=interrupt_callback)

loop()
