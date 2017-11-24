from asher._comps import _led
import asherHead
import time
my_led = _led.LED(channel=25)
my_led.start()
my_led.set_state(_led.LED.PULSE_QUICK)
time.sleep(4)
#my_led.stop()