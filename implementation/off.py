import machine
from time import time
from globals import POWER_OFF_DELAY, read_value, OFF_POTI_DELTA, OFF_REED_DELTA, STATES

# def deep_sleep(msecs):
#     # configure RTC.ALARM0 to be able to wake the device
#     rtc = machine.RTC()
#     rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

#     # set RTC.ALARM0 to fire after X milliseconds (waking the device)
#     rtc.alarm(rtc.ALARM0, msecs)

#     # put the device to sleep
#     machine.deepsleep()

transition_state = None
display = None
start_time = 0
reed_initial = 0
poti_initial = 0

def init(shared:dict, transition):
    global transition_state, start_time, display, reed_initial, poti_initial
    display = shared["display"]
    poti_initial = read_value(shared["poti"], shared["adc"])
    reed_initial = read_value(shared["reed"], shared["adc"])
    transition_state = transition
    start_time = time()
    remaining_time = POWER_OFF_DELAY - (time() - start_time)
    display.fill(0)
    display.text("Shutdown in:", 0, 0, 1)
    display.text(f"{remaining_time//60 :02}:{remaining_time%60 :02}", 0, 16, 1)
    display.show()
    pass


def run(shared:dict):
    remaining_time = POWER_OFF_DELAY - (time() - start_time)
    display.fill_rect(0, 16, 128, 32, 0)
    display.text(f"{remaining_time//60 :02}:{remaining_time%60 :02}", 0, 16, 1)
    display.show()

    if abs(poti_initial - read_value(shared["poti"], shared["adc"])) > OFF_POTI_DELTA or \
    abs(reed_initial - read_value(shared["reed"], shared["adc"])) > OFF_REED_DELTA:
        transition_state(STATES["idle"])
        return

    if remaining_time <= 0:
        shared["display"].poweroff()
        shared["buzz"].off()
        shared["poti"].off()
        shared["reed"].off()
        machine.deepsleep()