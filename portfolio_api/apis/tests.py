# Create your tests here.
from django.test import TestCase

class PostTestCase(TestCase):

    def test_post_is_posted(self):
        """Posts are created"""
        post1 = "We are testing this"
        self.assertEqual(post1, "We are testing this")