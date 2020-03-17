import unittest
from module import GuestList

class All_test(unittest.TestCase):
    def setUp(self):
        self.user = GuestList()
    
    def test_add_guest(self):
        self.user.add_guest('Edmond','black', 'Ugandan', 23, '0701207194')

        print(self.user.view())

    def test_user_exist(self):
        pass

    def test_user_deleted(self):
        self.user.add_guest('Edmond','black', 'Ugandan', 23, '0701207194')
        # self.assertEqual(self.guests__contain__(name))
        
