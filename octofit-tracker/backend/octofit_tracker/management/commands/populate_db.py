from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Define models for each collection
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'teams'

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'activities'

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'workouts'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(email='tony@marvel.com', name='Tony Stark', team='Marvel'),
            User(email='steve@marvel.com', name='Steve Rogers', team='Marvel'),
            User(email='clark@dc.com', name='Clark Kent', team='DC'),
            User(email='diana@dc.com', name='Diana Prince', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user_email='tony@marvel.com', type='Running', duration=30),
            Activity(user_email='steve@marvel.com', type='Cycling', duration=45),
            Activity(user_email='clark@dc.com', type='Swimming', duration=60),
            Activity(user_email='diana@dc.com', type='Yoga', duration=50),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=110)

        # Create workouts
        workouts = [
            Workout(name='Hero HIIT', difficulty='Hard'),
            Workout(name='Power Yoga', difficulty='Medium'),
            Workout(name='Speed Run', difficulty='Easy'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
