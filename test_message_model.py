"""Message model tests."""

# run these tests like:
#
#    python -m unittest test_message_model.py


import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError

from models import db, User, Message, Follows, connect_db

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler_test"

# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

connect_db(app)

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    def setUp(self):
        """ sets up the test environment """
        User.query.delete()

        u1 = User.signup("u1", "u1@email.com", "password", None)
        u2 = User.signup("u2", "u2@email.com", "password", None)

        db.session.commit()
        self.u1_id = u1.id
        self.u2_id = u2.id

        m1 = Message(text="m1-text", user_id=u1.id)
        db.session.add_all([m1])
        db.session.commit()

        self.m1_id = m1.id

        self.client = app.test_client()

    def tearDown(self):
        """ Rolls back the test environment and actions made in tests """
        db.session.rollback()


    def test_message_user_ref(self):
        """ Tests that message.user refers to correct user instance """
        message = Message.query.get(self.m1_id)
        user = User.query.get(self.u1_id)

        self.assertEqual(message.user, user)

    def test_user_message_ref(self):
        """ Tests that user.message refers to correct message instance """

        message = Message.query.get(self.m1_id)
        user = User.query.get(self.u1_id)

        self.assertIn(message, user.messages)

    def test_like_message(self):
        """ Tests that when a user likes a message it is in their
        messages liked"""


        user2 = User.query.get(self.u2_id)
        message = Message.query.get(self.m1_id)

        user2.messages_liked.append(message)
        db.session.commit()

        self.assertIn(message, user2.messages_liked)

    def test_user_likes(self):
        """ Tests that when a user likes a user is in users liked list
        of the message """

        user2 = User.query.get(self.u2_id)
        message = Message.query.get(self.m1_id)

        message.users_liked.append(user2)
        db.session.commit()

        self.assertIn(user2, message.users_liked)

