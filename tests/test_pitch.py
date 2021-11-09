from re import S
import unittest
from app.models import Pitch,User

class TestPitch(unittest.TestCase):
    def setUp(self):
        """Creates a new instance of the Pitch and User model."""
        self.new_user = User(username="reagan",email="123@gmail.com",password="cognito")
        self.new_pitch = Pitch(user_pitch="hello my name is reagan",user=self.new_user)
        
    def tearDown(self):
        """Deletes all user and pitch elements from the database after every test."""
        Pitch.query.delete()
        User.query.delete()
        
    def test_pitch_variables(self):
        """Checks if the pitch variables are correctly placed."""
        self.assertEquals(self.new_pitch.user_pitch,"hello my name is reagan")
        self.assertEquals(self.new_pitch.user,self.new_user)