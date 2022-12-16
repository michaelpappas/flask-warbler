"""User View tests."""

# run these tests like:
#
#    FLASK_DEBUG=False python -m unittest test_message_views.py


import os
from unittest import TestCase

from models import db, Message, User, connect_db

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler_test"

# Now we can import app

from app import app, CURR_USER_KEY, do_logout, do_login, session, g

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# This is a bit of hack, but don't use Flask DebugToolbar

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

connect_db(app)

db.drop_all()
db.create_all()

# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False


class UserViewTestCase(TestCase):
    def setUp(self):
        User.query.delete()

        u1 = User.signup("u1", "u1@email.com", "password", None)
        u2 = User.signup("u2", "u2@email.com", "password", None)
        db.session.flush()

        m1 = Message(text="m1-text", user_id=u1.id)
        db.session.add_all([m1])
        db.session.commit()

        self.u1_id = u1.id
        self.u2_id = u2.id
        self.m1_id = m1.id

        self.client = app.test_client()

    def test_auth_follower_page(self):
            """ Testing that logged in user can access followers page """
            with self.client as c:
                with c.session_transaction() as sess:
                    sess[CURR_USER_KEY] = self.u1_id

                user = User.query.get(self.u1_id)
                user2 = User.query.get(self.u2_id)
                user.followers.append(user2)
                db.session.commit()

                resp = c.get(f"/users/{self.u1_id}/followers")

                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn(f"<p>@{ user2.username }</p>", html)

    def test_auth_following_page(self):
        """ Testing that logged in user can access following page """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.u1_id

            user = User.query.get(self.u1_id)
            user2 = User.query.get(self.u2_id)
            user.followers.append(user2)
            db.session.commit()

            resp = c.get(f"/users/{ user2.id }/following")

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f"<p>@{ user.username }</p>", html)

    def test_unauth_access_home(self):
        """ Testing that unlogged in user sees sign up banner """
        with self.client as c:

            resp = c.get("/", follow_redirects=True)

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h4>New to Warbler?</h4>", html)

    def test_auth_access_home(self):
        """ Testing that logged in user sees user page """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.u1_id

            user = User.query.get(self.u1_id)

            resp = c.get("/", follow_redirects=True)

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f"<p>@{user.username}</p>", html)

    def test_unauth_following_page(self):
        """ Tests that you can't access following page when not logged in """
        with self.client as c:

            resp = c.get(f"/users/{self.u1_id}/following", follow_redirects=True)

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h4>New to Warbler?</h4>", html)

    def test_unauth_followers_page(self):
        """ Tests that you can't access followers page when not logged in """
        with self.client as c:

            resp = c.get(f"/users/{self.u1_id}/followers", follow_redirects=True)

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h4>New to Warbler?</h4>", html)