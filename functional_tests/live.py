from .tests import NewVisitorTest

class LiveTest(NewVisitorTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.server_url = 'http://app-staging.mattround.net'
        
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()