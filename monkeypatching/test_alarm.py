import unittest
from unittest.mock import patch, Mock

from .alarm import Alarm


class AlarmTest(unittest.TestCase):

    def test_check_with_too_high_pressure(self):
        with patch('monkeypatching.alarm.Sensor') as test_sensor_class:
            test_sensor_instance = Mock()
            test_sensor_instance.sample_pressure.return_value = 22
            test_sensor_class.return_value = test_sensor_instance
            alarm = Alarm()
            alarm.check()
            self.assertTrue(alarm.is_alarm_on)

    @patch('monkeypatching.alarm.Sensor')
    def test_check_with_too_low_pressure(self, test_sensor_class):
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 15
        test_sensor_class.return_value = test_sensor_instance
        alarm = Alarm()
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)
