class MyService(object):
    """Contains three different implementation of handle_request for testing
    Second and third are wrong
    """

    def __init__(self, sso_registry):
        self.sso_registry = sso_registry

    def handle_request_correctly(self, request, token):
        if self.sso_registry.is_valid(token):
            return 'Hello world'
        return 'Please enter your login details'

    def handle_request_wrong_token(self, request, token):
        if self.sso_registry.is_valid(None):
            return 'Hello world'
        return 'Please enter your login details'

    def handle_request_no_call_to_is_valid(self, request, token):
        if token:
            return 'Hello world'
        return 'Please enter your login details'

    handle_request = handle_request_wrong_token

