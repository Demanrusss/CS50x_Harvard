from datetime import datetime, timedelta
from sqlite3 import Timestamp
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        user = User(username = 'susan')
        user.set_password('test_password')
        self.assertFalse(user.check_password('another_password'))
        self.assertTrue(user.check_password('test_password'))

    def test_avatar(self):
        user = User(username = 'john', email = 'john@test.com')
        self.assertEqual(user.avatar(128), 
                         ('https://www.gravatar.com/avatar/11111111?d=robohash&s=128'))

    def test_follow(self):
        user1 = User(username = 'john', email = 'john@test.com')
        user2 = User(usernam = 'susan', email = 'susan@test.com')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        self.assertEqual(user1.followed.all(), [])
        self.assertEqual(user2.followed.all(), [])

        user1.follow(user2)
        db.session.commit()
        self.assertTrue(user1.is_following(user2))
        self.assertEqual(user1.followed.count(), 1)
        self.assertEqual(user1.followed.first().username, 'susan')
        self.assertEqual(user2.followers.count(), 1)
        self.assertEqual(user2.followers.first().username, 'john')

        user1.unfollow(user2)
        db.session.commit()
        self.assertFalse(user1.is_following(user2))
        self.assertEqual(user1.followed.count(), 0)
        self.assertEqual(user2.followers.count(), 0)

    def test_follow_posts(self):
        # create four users
        user1 = User(username = 'john', email = 'john@test.com')
        user2 = User(username = 'susan', email = 'susan@test.com')
        user3 = User(username = 'david', email = 'david@test.com')
        user4 = User(username = 'alex', email = 'alex@test.com')
        db.session.add_all([user1, user2, user3, user4])

        # create four posts
        now = datetime.utcnow()
        post1 = Post(body = 'test post from john', 
                     author = user1, 
                     timestamp = now + timedelta(seconds = 1))
        post2 = Post(body = 'test post from susan', 
                     author = user2, 
                     timestamp = now + timedelta(seconds = 10))
        post3 = Post(body = 'test post from david', 
                     author = user3, 
                     timestamp = now + timedelta(seconds = 5))
        post4 = Post(body = 'test post from alex', 
                     author = user4, 
                     timestamp = now + timedelta(seconds = 7))
        db.session.add_all([post1, post2, post3, post4])
        db.session.commit()

        #setup the followers
        user1.follow(user2)
        user1.follow(user4)
        user2.follow(user3)
        user3.follow(user4)
        db.session.commit()

        # check the followed posts of each user
        follower1 = user1.followed_posts().all()
        follower2 = user2.followed_posts().all()
        follower3 = user3.followed_posts().all()
        follower4 = user4.followed_posts().all()
        self.assertEqual(follower1, [post2, post4, post1])
        self.assertEqual(follower2, [post3, post2])
        self.assertEqual(follower3, [post4, post3])
        self.assertEqual(follower4, [post4])

if __name__ == '__main__':
    unittest.main(verbosity = 2)