import unittest
from userdetails import User, Credentials


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        test setup method
        '''
        self.new_user = User("patel", "patel")

    def test_init(self):
        '''
        test initialization
        '''
        self.assertEqual(self.new_user.user_name, "patel")
        self.assertEqual(self.new_user.password, "patel")

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

        test_user = User("patel", "patel")
        test_user.save_user()

        self.assertEqual(len(User.user_list), 2)

    def test_find_user(self):
        '''
        test to check for a specific user using their name
        '''
        self.new_user.save_user()

        test_user = User("patel", "patel")
        test_user.save_user()

        user_found = User.find_by_name("patel")
        self.assertEqual(user_found.password, test_user.password)
class TestCredentials(unittest.TestCase):
    '''
    test for Credential
    '''

    def setUp(self):
        '''
        test setup method
        '''

        self.new_credential = Credentials("intagram","pass123")

    def test_init(self):
        '''
        test initilalization
        '''
        self.assertEqual(self.new_credential.account_name,"facebook")
        self.assertEqual(self.new_credential.account_password,"pass123456")


    def test_save_account(self):
        '''
        test to see if new credentials are saved in our credential_list
        '''
        self.new_credential.save_account()
        self.assertEqual(len(Credentials.credential_list),1)

    def tearDown(self):
        '''
        clear our credential_list
        '''
        Credentials.credential_list = []


    def test_save_multiple_account(self):
        '''
        test ability to save more than one credentials
        '''
        self.new_credential.save_account()
        test_account = Credentials("Telegram","pass12345")
        test_account.save_account()

        self.assertEqual(len(Credentials.credential_list),2)



if __name__ == '__main__':
    unittest.main(verbosity=2)
