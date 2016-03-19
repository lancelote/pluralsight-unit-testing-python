from .sensor import Sensor


class Alarm(object):

    def __init__(self):
        self._low_pressure_threshold = 17
        self._high_pressure_threshold = 21
        self._sensor = Sensor()
        self._is_alarm_on = False

    def check(self):
        psi_pressure_value = self._sensor.sample_pressure()
        if psi_pressure_value < self._low_pressure_threshold or \
                psi_pressure_value > self._high_pressure_threshold:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on
