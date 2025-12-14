from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Avengers assemble! Champions of fitness and teamwork.'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League! Defenders of health and wellness.'
        )

        self.stdout.write('Creating users...')
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team_id=str(team_marvel._id)),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team_id=str(team_marvel._id)),
            User.objects.create(name='Captain America', email='captainamerica@marvel.com', team_id=str(team_marvel._id)),
            User.objects.create(name='Black Widow', email='blackwidow@marvel.com', team_id=str(team_marvel._id)),
            User.objects.create(name='Thor', email='thor@marvel.com', team_id=str(team_marvel._id)),
            User.objects.create(name='Batman', email='batman@dc.com', team_id=str(team_dc._id)),
            User.objects.create(name='Superman', email='superman@dc.com', team_id=str(team_dc._id)),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team_id=str(team_dc._id)),
            User.objects.create(name='Flash', email='flash@dc.com', team_id=str(team_dc._id)),
            User.objects.create(name='Aquaman', email='aquaman@dc.com', team_id=str(team_dc._id)),
        ]

        self.stdout.write('Creating activities...')
        activities_data = [
            {'user': users[0], 'type': 'Running', 'duration': 45, 'calories': 400},
            {'user': users[0], 'type': 'Web Swinging', 'duration': 60, 'calories': 500},
            {'user': users[1], 'type': 'Strength Training', 'duration': 90, 'calories': 600},
            {'user': users[1], 'type': 'Flying', 'duration': 30, 'calories': 350},
            {'user': users[2], 'type': 'Shield Training', 'duration': 60, 'calories': 450},
            {'user': users[2], 'type': 'Running', 'duration': 120, 'calories': 800},
            {'user': users[3], 'type': 'Martial Arts', 'duration': 75, 'calories': 550},
            {'user': users[3], 'type': 'Running', 'duration': 40, 'calories': 380},
            {'user': users[4], 'type': 'Hammer Training', 'duration': 90, 'calories': 700},
            {'user': users[4], 'type': 'Lightning Power', 'duration': 45, 'calories': 500},
            {'user': users[5], 'type': 'Martial Arts', 'duration': 120, 'calories': 900},
            {'user': users[5], 'type': 'Night Patrol', 'duration': 180, 'calories': 1000},
            {'user': users[6], 'type': 'Flying', 'duration': 60, 'calories': 450},
            {'user': users[6], 'type': 'Strength Training', 'duration': 90, 'calories': 650},
            {'user': users[7], 'type': 'Sword Training', 'duration': 75, 'calories': 550},
            {'user': users[7], 'type': 'Running', 'duration': 50, 'calories': 420},
            {'user': users[8], 'type': 'Speed Training', 'duration': 30, 'calories': 600},
            {'user': users[8], 'type': 'Running', 'duration': 20, 'calories': 500},
            {'user': users[9], 'type': 'Swimming', 'duration': 90, 'calories': 700},
            {'user': users[9], 'type': 'Underwater Training', 'duration': 120, 'calories': 800},
        ]
        
        for activity_data in activities_data:
            Activity.objects.create(
                user_id=str(activity_data['user']._id),
                activity_type=activity_data['type'],
                duration=activity_data['duration'],
                calories=activity_data['calories'],
                date=date.today()
            )

        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = [
            {'user': users[5], 'points': 1900, 'rank': 1},  # Batman
            {'user': users[6], 'points': 1100, 'rank': 2},  # Superman
            {'user': users[9], 'points': 1500, 'rank': 3},  # Aquaman
            {'user': users[1], 'points': 950, 'rank': 4},   # Iron Man
            {'user': users[2], 'points': 1250, 'rank': 5},  # Captain America
            {'user': users[4], 'points': 1200, 'rank': 6},  # Thor
            {'user': users[8], 'points': 1100, 'rank': 7},  # Flash
            {'user': users[7], 'points': 970, 'rank': 8},   # Wonder Woman
            {'user': users[3], 'points': 930, 'rank': 9},   # Black Widow
            {'user': users[0], 'points': 900, 'rank': 10},  # Spider-Man
        ]
        
        for lb_data in leaderboard_data:
            Leaderboard.objects.create(
                user_id=str(lb_data['user']._id),
                total_points=lb_data['points'],
                rank=lb_data['rank']
            )

        self.stdout.write('Creating workouts...')
        workouts = [
            {
                'name': 'Super Strength Circuit',
                'description': 'Build superhuman strength with this intense circuit training',
                'difficulty': 'Hard',
                'target_muscles': ['chest', 'arms', 'shoulders']
            },
            {
                'name': 'Speed Training',
                'description': 'Improve your speed and agility like a speedster',
                'difficulty': 'Medium',
                'target_muscles': ['legs', 'core', 'cardio']
            },
            {
                'name': 'Hero Core Workout',
                'description': 'Strengthen your core for better stability and power',
                'difficulty': 'Medium',
                'target_muscles': ['abs', 'core', 'back']
            },
            {
                'name': 'Endurance Challenge',
                'description': 'Build stamina and endurance for long battles',
                'difficulty': 'Hard',
                'target_muscles': ['full body', 'cardio']
            },
            {
                'name': 'Beginner Hero Training',
                'description': 'Start your hero journey with this beginner-friendly workout',
                'difficulty': 'Easy',
                'target_muscles': ['full body']
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with superhero test data!'))
