import time
from time import sleep
import gpiozero as gpiozero
from gpiozero import Button, LED

stop_button= Button(23)
go_button= Button(21)
led_green= LED(12)
led_red= LED(25)

def go_button_press():
    return go_button.is_pressed
    


def stop_button_press():
    return stop_button.is_pressed




def green_led_on():
    led_green.on()
    
def green_led_off():
    led_green.off()

def red_led_on():
    led_red.on()
    
def red_led_off():
    led_red.off()


green_led_on()
sleep(1)
green_led_off()