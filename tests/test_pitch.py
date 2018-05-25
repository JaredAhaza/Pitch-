import unittest
from app.models import Pitch, User

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_James = User(
            username='James', password='potato', email='james@ms.com')
        self.new_pitch = Pitch(title='Elevator Pitch Example for an Professional Accountant',body="Test Pitch",author='Improv Andy',category='business',upvotes=1,downvotes=0,user=self.user_James)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_save_pitch(self):
        self.new_pitch.save_pitches()
        self.assertTrue(len(Pitch.query.all()) > 0)