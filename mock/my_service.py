class MyService(object):

    def __init__(self, sso_registry):
        self.sso_registry = sso_registry

    def handle_request(self, request, token):
        if self.sso_registry.is_valid(token):
            return 'Hello world'
        return 'Please enter your login details'
