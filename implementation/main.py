import off
import idle
import timer_running
import beep
from globals import STATES

from machine import Pin, I2C, ADC
import ssd1306
import time

i2c = None
display = None
adc = None
poti = None
reed = None
buzz = None
shared_data = None
current_state = 0


def init():
    global i2c, display, adc, poti, reed, buzz, shared_data, current_state 
    print(__name__)
    # startup
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    display = ssd1306.SSD1306_I2C(128, 32, i2c)
    display.text("Booting...", 0, 0, 1)
    display.show()
    adc = ADC(0)
    poti = Pin(12, Pin.OUT)
    reed = Pin(14, Pin.OUT)
    buzz = Pin(13)

    # State machine
    shared_data = {
        "display": display,
        "poti": poti,
        "reed": reed,
        "buzz": buzz,
        "adc": adc,
        "temp": None
    }
    current_state = 1


def transition_state(state:int):
    global current_state
    print(f"transition to {state}")
    current_state = state
    if state == 0:
        off.init(shared_data, transition_state)
    elif state == 1:
        idle.init(shared_data, transition_state)
    elif state == 2:
        timer_running.init(shared_data, transition_state)
    elif state == 3:
        beep.init(shared_data, transition_state)
    
    return state


def main():
    transition_state(1)
    while(True):
        if current_state == 0:
            off.run(shared_data)
        elif current_state == 1:
            idle.run(shared_data)
        elif current_state == 2:
            timer_running.run(shared_data)
        elif current_state == 3:
            beep.run(shared_data)
        time.sleep(0.1)


init()
main()
    