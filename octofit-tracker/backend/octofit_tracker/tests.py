from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Test Hero',
            email='test@hero.com',
            team_id='test123'
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test Hero')
        self.assertEqual(self.user.email, 'test@hero.com')
        self.assertEqual(str(self.user), 'Test Hero')

class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team'
        )
    
    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(str(self.team), 'Test Team')

class APIEndpointTest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team'
        )
        self.user = User.objects.create(
            name='Test Hero',
            email='test@hero.com',
            team_id=str(self.team._id)
        )
    
    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
    
    def test_users_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_teams_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Test Hero',
            email='test@hero.com'
        )
        self.activity = Activity.objects.create(
            user_id=str(self.user._id),
            activity_type='Running',
            duration=30,
            calories=200,
            date=date.today()
        )
    
    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 200)

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout',
            difficulty='Medium',
            target_muscles=['legs', 'core']
        )
    
    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.difficulty, 'Medium')
        self.assertEqual(str(self.workout), 'Test Workout')
