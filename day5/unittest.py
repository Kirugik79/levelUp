
import unittest

from Flask_sessions import *

class LoginSessions(unittest.TestCase):

    def setUp(self):
        self.dictionary = Username ({}, [], "username", "Password", "first_namne", "second_name", "email" "comment")

    def test_if_user_is_registered(self):
        self.assertEqual (self.dictionary [username{}] == ["username"])

    def test_if_user_is_logged_in(self):
        self.assertEqual({}, self.dictionary [username][password]


    def test_if_user_can_make_comment(self):
        self.assertEqual(self.dictionary ["username"] ==(self.dictionary ["password"])

    def test_if_user_can_fetch_comments(self):
        self.assertEqual(self.dictionary (username = self.dictionary [username]))

if __name__ == '__main__':
    unittest.main()
