import time
import gpiozero as gpiozero

def go_button_press():
    gpiozero.setmode(gpiozero.BCM)
    gpiozero.setup(21,gpiozero.IN)
    if gpiozero.input(21):
        print("Go")
        return True
    else:
        
        return False


def stop_button_press():
    gpiozero.setmode(gpiozero.BCM)
    gpiozero.setup(23,gpiozero.IN)
    if gpiozero.input(23):
        print("stop")
        return True
    else:
        return False

go_button_press()
    