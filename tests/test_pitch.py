import unittest
from app.models import Pitch,User
from app import db

class TestPitch(unittest.TestCase):
    def setUp(self):
        """Creates a new instance of the Pitch and User model."""
        self.new_user = User(username="reagan",email="123@gmail.com",password="cognito")
        self.new_pitch = Pitch(user_pitch="hello my name is reagan",user=self.new_user)
        
    def tearDown(self):
        """Deletes all user and pitch elements from the database after every test."""
        Pitch.query.delete()
        User.query.delete()
        db.session.commit()
        
    def test_pitch_variables(self):
        """Checks if the pitch variables are correctly placed."""
        self.assertEquals(self.new_pitch.user_pitch,"hello my name is reagan")
        self.assertEquals(self.new_pitch.user_id,self.new_user.id)
        
    def test_save_pitch(self):
        """Checks if the pitch is being saved."""
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)
        
    def test_get_pitches_by_user_id(self):
        """Checks if a user's pitches are being listed."""
        self.new_pitch.save_pitch()
        got_user_pitches = Pitch.get_user_pitches(self.new_pitch.user_id)
        self.assertTrue(len(got_user_pitches) == 1)
        
    def test_get_pitches(self):
        """Checks if all pitches are returned."""
        self.new_pitch.save_pitch()
        self.second_user = User(username="brett",email="456@gmail.com",password="yesman")
        self.second_pitch = Pitch(user_pitch="hello my name is brett",user=self.second_user)
        self.second_pitch.save_pitch()
        got_pitches = Pitch.get_all_pitches()
        self.assertTrue(len(got_pitches) == 2)

        
