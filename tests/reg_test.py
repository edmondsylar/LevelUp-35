import unittest
from module.signup import user_reg

class all_tests(unittest.TestCase):
    
    def setUp(self):
        self.tester = user_reg()

    def test_form_exist(self):
        self.assertIsInstance(self.tester, user_reg)
        
    def test_user_name_exist(self):
        self.tester.add_user('test_user', 'test_user@example.com', 'sec98393484sec')
        self.assertNotEqual(self.tester.user['username'], '')

    def test_email_provided(self):
        self.tester.add_user('test_user', 'test_user@example.com', 'sec98393484sec')
        self.assertNotEqual(self.tester.user['email'], '')

    def test_password_provided(self):
        self.tester.add_user('test_user', 'test_user@example.com', 'sec98393484sec')
        self.assertNotEqual(self.tester.user['Security key'], '')
