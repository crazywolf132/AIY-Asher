import logging
import os.path
import time
import asherHead

logger = logging.getLogger('status_ui')

class _StatusUi(object):

    def __init__(self):
        self._trigger_sound_wave = None
        self._state_map = {
            "starting": asherHead.LED.PULSE_QUICK,
            "ready": asherHead.LED.BEACON_DARK,
            "listening": asherHead.LED.ON,
            "thinking": asherHead.LED.PULSE_QUICK,
            "stopping": asherHead.LED.PULSE_QUICK,
            "power-off": asherHead.LED.OFF,
            "error": asherHead.LED.BLINK_3,
        }
        asherHead.get_led().set_state(asherHead.LED.OFF)

    def status(self, status):
        if status not in self._state_map:
            logger.warning("unspported state: %s, must be on of the %s", status, ",".join(self._state_map.keys()))
            return False
        asherHead.get_led().set_state(self._state_map[status])
        return True