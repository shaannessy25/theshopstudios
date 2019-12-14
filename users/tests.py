# wiki/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from users.model import Profile

class ProfileTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)


class ViewPostTest(TestCase):
    """Tests that the pagea works."""
    def test_route(self):
        user = User.objects.create()
        self.client.force_login(user)
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/')
    
        self.assertEqual(response.status_code, 200)

class ViewProfileTest(TestCase):
    """Tests that the pagea works."""
    def test_route(self):
        user = User.objects.create()
        self.client.force_login(user)
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/profile/')
    
        self.assertEqual(response.status_code, 200)

class CreatePostTest(TestCase):
    """Tests that the pagea works."""
    def test_route(self):
        user = User.objects.create()
        self.client.force_login(user)
       
        #Make a GET request, and test route returns 200
        response = self.client.get('/create_new/')
    
        self.assertEqual(response.status_code, 200)