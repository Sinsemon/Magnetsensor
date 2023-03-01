from machine import PWM
from time import time
from globals import STATES, read_value, BEEP_TIME_OFF, DEVELOPMENT

display = None
transition_state = None
pwm = None
start_time = 0

def init(shared:dict, transition):
    global display, transition_state, pwm, start_time
    transition_state = transition
    if (read_value(shared["reed"], shared["adc"]) > 900) != DEVELOPMENT: # TODO ändern zu >
        transition_state(1) # idle
        return
    display = shared["display"]
    display.fill(0)
    display.text("Buzzing", 0, 0, 1)
    display.text("Close Window!", 0, 16, 1)
    display.show()
    start_time = time()
    pwm = PWM(shared["buzz"], freq=500, duty=512)

def run(shared:dict):
    global pwm
    _reed = read_value(shared["reed"], shared["adc"])
    if (_reed > 900) != DEVELOPMENT: # TODO ändern zu > 
        pwm.deinit()
        transition_state(STATES["idle"])
    elif (time() - start_time) > BEEP_TIME_OFF:
        pwm.deinit()
        transition_state(STATES["off"])


