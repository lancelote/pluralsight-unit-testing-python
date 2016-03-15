import unittest

from .my_service import MyService
from .fake_single_sign_on_registry import (
    FakeSingleSignOnRegistry,
    MockSingleSignOnRegistry,
    SpySingleSignOnRegistry,
    SSOToken,
)


class MyServiceTest(unittest.TestCase):

    def test_invalid_token(self):
        registry = FakeSingleSignOnRegistry()
        my_service = MyService(registry)

        response = my_service.handle_request('Do stuff', token=None)
        self.assertIn('Please enter your login details', response)

    def test_valid_token(self):
        registry = FakeSingleSignOnRegistry()
        token = registry.register('Valid credentials')
        my_service = MyService(registry)

        response = my_service.handle_request('Do stuff', token)
        self.assertIn('Hello world', response)

    def test_invalid_token_with_mock(self):
        token = SSOToken()
        registry = MockSingleSignOnRegistry(expected_token=token,
                                            token_is_valid=False)
        my_service = MyService(registry)

        my_service.handle_request('Do stuff', token=token)
        self.assertTrue(registry.is_valid_was_called)

    def test_valid_token_with_mock(self):
        token = SSOToken()
        registry = MockSingleSignOnRegistry(expected_token=token,
                                            token_is_valid=True)
        my_service = MyService(registry)

        my_service.handle_request('Do stuff', token=token)
        self.assertTrue(registry.is_valid_was_called)

    def test_invalid_token_with_spy(self):
        token = SSOToken()
        registry = SpySingleSignOnRegistry(accept_all_tokens=False)
        my_service = MyService(registry)

        my_service.handle_request('Do stuff', token=token)
        self.assertIn(token, registry.checked_tokens)

    def test_valid_token_with_spy(self):
        token = SSOToken()
        registry = SpySingleSignOnRegistry(accept_all_tokens=True)
        my_service = MyService(registry)

        my_service.handle_request('Do stuff', token=token)
        self.assertIn(token, registry.checked_tokens)
