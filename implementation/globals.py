DEVELOPMENT = False
IDLE_TIME_OFF = 15 if not DEVELOPMENT else 5 # Time after which the MC powers off in idle state
BEEP_TIME_OFF = 120 if not DEVELOPMENT else 1# Time after which the MC poweres of in beep state
POWER_OFF_DELAY = 5 # Countdown time before power off
OFF_POTI_DELTA = 50 # The difference in measurement of the Poti to prevent shutdown
OFF_REED_DELTA = 50 # The difference in measurement of the Reed to prevent shutdown

STATES = {
    "off": 0,
    "idle": 1,
    "timer_running": 2,
    "beep": 3
}

def read_value(pin, adc) -> int:
    pin.on()
    _val = adc.read()
    pin.off()
    return _val