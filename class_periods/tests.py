from django.test import TestCase, Client
from rest_framework.test import APIClient

from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ClassroomSessionTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="testuser",
            password="wowpassword"
        )
        ClassPeriods.objects.create(
            name="TestClass1",
            location="CB1",
            description="Fundamentals of Testing 1",
            prefix="TST",
            code="1001",
            owner=user
        )
        c = Client()
        response = c.post('/api/classes/token', data={
                'username': 'testuser',
                'password': 'wowpassword'
                }
               )
        self.assertIsNotNone(response.json()['access'])
        self.assertIsNotNone(response.json()['refresh'])
        self.token = response.json()['access']
    
    def testUser(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.username,"testuser")

    def testUserOwnsClass(self):
        class_period = ClassPeriods.objects.get(name="TestClass1")
        user = User.objects.get(username="testuser")
        self.assertEqual(class_period.owner, user)
    
    def testSessionCreationLifecycle(self):   
        c = APIClient()
        # c.login(username='testuser', password='wowpassword')
        c.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        # Request a Token
        response = c.post('/api/classes/requestToken', data = {
            'token': 'TESTTOKEN',
            'class_name': 'TestClass1'
        })

        self.assertIsNotNone(response.json())
        self.assertEqual(response.status_code, 200)

        tokens = StudentCheckin.objects.all()
        # Validate the Token
        response = c.post('/api/classes/validateToken', data = {
            'token': 'TESTTOKEN',
            'name': 'TESTSTUDENTlk',
            'pid': '1234567890',
            'hwid': 'asdfasdf'
        })
        # print(response.json())

        self.assertEqual(response.status_code, 200)
        # print(response.)
        # self.assertIsNotNone(response.json())

        # Attempt second validation for user, expect repetition error
        response = c.post('/api/classes/validateToken', data = {
            'token': 'TESTTOKEN',
            'name': 'TESTSTUDENTlk',
            'pid': '1234567890',
            'hwid': 'asdfasdf'
        })

        self.assertIsNotNone(response.json())
        self.assertEqual(response.json()['error'], 'Already Checked In')
        
        # Invalidate the token

        response = c.post('/api/classes/invalidateToken', data = {
            'token': 'TESTTOKEN'
        })

        self.assertEqual(response.status_code, 200)
        