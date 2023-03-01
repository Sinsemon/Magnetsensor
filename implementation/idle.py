from time import time
from globals import read_value, STATES, IDLE_TIME_OFF, DEVELOPMENT

display = None
transition_state = None
start_time = 0


def init(shared:dict, transition):
    global display, transition_state, start_time
    start_time = time()
    display = shared["display"]
    transition_state = transition
    display.fill_rect(0, 0, 128, 16, 0)
    display.text("Set time:", 0, 0, 1)
    display.show()


def run(shared:dict):
    if time() - start_time > IDLE_TIME_OFF:
        transition_state(STATES["off"])
        return

    # read poti and reed
    _poti = read_value(shared["poti"], shared["adc"]) # max value = 950
    _reed = read_value(shared["reed"], shared["adc"])
    print(_poti, _reed)
    
    display.fill_rect(0, 16, 128, 32, 0)
    display.text(f"Timer: {_poti//60 :02}:{_poti%60 :02}", 0, 16, 1)
    display.show()

    if (_reed < 900) != DEVELOPMENT: # TODO ändern zu <
        shared["temp"] = (time(), _poti) # time since reset in seconds
        transition_state(STATES["timer_running"])