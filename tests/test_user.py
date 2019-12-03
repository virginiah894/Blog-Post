import unittest
from app.models import User,Post

class UserModelTest(unittest.TestCase):

# instantiating the user from the class User
    def setUp(self):
    self.new_user = User(password = 'perry')
# test to confirmif the password is being typed
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        # confirms that password isnt exposed
    def test_no_access_password(self):
      with self.assertRaises(AttributeError):
        self.new_user.password
# test for passord verification
    def test_password_verification(self):
      self.assertTrue(self.new_user.verify_password('perry'))