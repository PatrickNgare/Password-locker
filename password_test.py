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

    def test_save_user(self):
        '''
        see if the user is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
    def tearDown(self):
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test if multiple users will be saved
        '''
        self.new_user.save_user()

        test_user = User("patel", "678910")
        test_user.save_user()

        self.assertEqual(len(User.user_list), 2)
