from gpiozero import LED, Button
from time import sleep

led = LED(27)
button = Button(2)

button.when_pressed = led.on
button.when_released= led.off

pause()
