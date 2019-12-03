 unittest
from app.models import Post,User
from app import db
class TestModelPost(unittest.TestCase)
    def setUp(self):
      self.user_mukabi = User(username = 'Mukabi',password = 'perry', email = 'vkengara@gmail.com')
  
      self.new_ = Post(title = title,date)
# deletes everything after each test
    def tearDown(self):
      Post.query.delete()
      User.query.delete()

  # test to check if items are properly placed
    def test_check_instance_variables(self):
      self.assertEquals(self.new_post.post.id,1)
      self.assertEquals(self.new_post.post_update,'good')
      self.assertEquals(self.new_post.user,self.user_mukabi)
    def test_save_post(self):
      self.new_post.save_post()
      self.assertTrue(len(Post.query.all())>0)
    def test_get_post_by_id(self):
      self.new_post.save_post()
      got_posts = Post.get_posts(1)
      self.assertTrue(len(got_posts) == 1)
