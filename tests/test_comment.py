import unittest
from app.models import Pitch,User,Comment
from app import db

class TestComment(unittest.TestCase):
    def setUp(self):
        """Creates a new instance of the Comment,Pitch, and User Models."""
        self.new_user = User(username="reagan",email="123@gmail.com",password="cognito")
        self.new_pitch = Pitch(user_pitch="hello my name is reagan",user=self.new_user)
        self.new_comment= Comment(comment="good job!",)
    def tearDown(self):
        """Deletes all user, comment, and pitch elements from the test-database after every test."""
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()
        db.session.commit()
        
    def test_comment_variables(self):
        """Checks if the comment variables are correctly placed."""
        self.assertEquals(self.new_comment.comment,"good job!")
        self.assertEquals(self.new_comment.user_id,self.new_user.id)
        self.assertEquals(self.new_comment.pitch_id,self.new_pitch.id)

    def test_save_comment(self):
        """Checks if the comment is saved to the databse."""
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
        
    def test_get_pitches_by_user_id(self):
        """Checks if comments belonging to a pitch are listed."""
        self.new_comment.save_comment()
        got_comments = Comment.get_pitch_comments(self.new_comment.pitch_id)
        self.assertTrue(len(got_comments) == 1)
