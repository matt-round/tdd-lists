from .tests import NewVisitorTest

class LiveTest(NewVisitorTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.server_url = 'http://app.mattround.net'
        
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()