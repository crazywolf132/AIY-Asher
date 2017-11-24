import asher._comps._led
import asher._comps._status_ui

_GPIO_BUTTON = 23
_GPIO_LED = 25

LED = asher._comps._led.LED
_asherHead_led = None
_status_ui = None

def get_led():
    global _asherHead_led
    if _asherHead_led is None:
        _asherHead_led = asher._comps._led.LED(channel = _GPIO_LED)
        _asherHead_led.start()
    return _asherHead_led

def get_status_ui():
    global _status_ui
    if _status_ui is None:
        _status_ui = asher._comps._status_ui._StatusUi()
    return _status_ui