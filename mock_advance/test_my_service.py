import unittest

from .my_service import MyService
from .single_sign_on import *


class MyServiceTest(unittest.TestCase):

    def test_invalid_token(self):
        registry = FakeSingleSignOnRegistry()
        my_service = MyService(registry)

        response = my_service.handle_request('do stuff', token=None)
        self.assertIn('please enter your login details', response)
