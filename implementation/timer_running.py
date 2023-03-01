from time import time
from globals import read_value, STATES, DEVELOPMENT


transition_state:Callable = None
start_time = 0
duration = 0
remaining_old = 0
display = None

def init(shared:dict, transition):
    global start_time, duration, display, transition_state
    transition_state = transition
    start_time, duration = shared["temp"]
    delta = duration - (time() - start_time)
    display = shared["display"]
    display.fill(0)
    display.text("Timer started", 0, 0, 1)
    display.fill_rect(0, 16, 128, 32, 0)
    display.text(f"Timer: {delta//60 :02}:{delta%60 :02}", 0, 16, 1)
    display.show()



def run(shared:dict):
    global remaining_old
    remaining_time = duration - (time() - start_time)
    _reed = read_value(shared["reed"], shared["adc"])
    
    if remaining_time <= 0:
        transition_state(STATES["beep"])
        return
    elif (_reed > 900) != DEVELOPMENT: # TODO change to >
        transition_state(STATES["idle"])
        return
    
    if remaining_old != remaining_time:
        display.fill_rect(0, 16, 128, 32, 0)
        display.text(f"Timer: {remaining_time//60 :02}:{remaining_time%60 :02}", 0, 16, 1)
        display.show()
        remaining_old = remaining_time

# sollte 5:05 laufen läuft aber 5:30 min


