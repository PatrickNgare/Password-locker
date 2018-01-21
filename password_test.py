import unittest
from password import User, Credentials


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        test setup method
        '''
        self.new_user = User("Patrick", "Patrick1234")

    def test_init(self):
        '''
        test initialization
        '''
        self.assertEqual(self.new_user.user_name, "Patrick")
        self.assertEqual(self.new_user.password, "Patrick1234")
