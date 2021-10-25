import unittest
from user import Info
import pyperclip as pc
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        method to run each test
        '''
        self.user = User("Feddy", "7114")

    def test_init(self):
        '''
        check proper user initialization
        '''
        self.assertEqual(self.user.username, "Feddy")
        self.assertEqual(self.user.password, "7114")

    def tearDown(self):
        '''
        method to clean up after each test
        '''

        User.userList = []

    def test_save_multiple_users(self):
        '''
        method to test multiple saved users
        '''
        self.user.saveUser()
        test_user = User("Don", "611")  # new contact
        test_user.saveUser()

        self.assertEqual(len(User.userList), 2)

    def test_delete_user(self):
        """
        delete users
        """
        self.user.saveUser()
        test_user = User("Don", "611")  # new contact
        test_user.saveUser()

        self.user.deleteUser()
        self.assertEqual(len(User.userList), 1)

    def test_display_users(self):
        """
        method to test if users are correctly displayed
        """
        self.assertEqual(User.displayUser(), User.userList)


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        define the constructor
        """
        self.info = Info("Facebook", "fb", "565641")

    def tearDown(parameter_list):
        """
        clear up during each test
        """
        pass

    def test_init(self):
        """
        make sure the constructor is well initialized
        """
        self.assertEqual(self.info.account, "Facebook")
        self.assertEqual(self.info.username, "fb")
        self.assertEqual(self.info.password, "565641")

    def test_save_multiples_info(self):
        """
        test for multiple info
        """
        self.info.save_details()
        test_info = Info("Facebook", "fb", 565641)  # new contact
        test_info.save_details()

        self.assertEqual(len(Info.info_list), 3)

    def test_delete(self):
        """
        test if the onfo can be deleted
        
        """
        self.info.save_details()
        test_info = Info("Facebook", "fb", 565641)  # new contact
        test_info.save_details()

        self.info.delete_info()
        self.assertEqual(len(Info.info_list), 1)

    def  test_find_info(self):
        """
        search a info
        """
        self.info.find_info("Facebook")
        test_info = Info("Facebook", "fb", 565641)  # new contact
        test_info.find_info("Facebook")

        found = Info.find_info("Facebook")
        self.assertEqual(found.account, test_info.account)

    def test_display(self):
        """
        method to test if info can be displayed
        """
        self.assertEqual(Info.display_info(),Info.info_list)


if __name__ == "__main__":
    unittest.main()