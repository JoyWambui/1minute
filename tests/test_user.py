from operator import is_not
import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        """Creates a new instance of the USer model."""
        self.new_user = User(username="reagan",email="123@gmail.com",password="cognito")
        
    def tearDown(self):
        """Deletes all user elements frrom the database after every test."""
        User.query.delete()
        
    def test_user_variables(self):
        """Checks if the user variables are correctly placed."""
        self.assertEquals(self.new_user.username,"reagan")
        self.assertEquals(self.new_user.email,"123@gmail.com")
        

    def test_sets_password(self):
        """Checks if the user password contains a value and is being hashed."""
        self.assertTrue(self.new_user.user_password is not None)

    def test_no_access_password(self):
        """Confirms that app raises an attribute error when trying to access the password property."""
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        """Checks if a correct input password and a hashed password can be verified."""
        self.assertTrue(self.new_user.password_verification("cognito"))

