from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team_id']
    
    def get_id(self, obj):
        return str(obj._id)

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description']
    
    def get_id(self, obj):
        return str(obj._id)

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration', 'calories', 'date']
    
    def get_id(self, obj):
        return str(obj._id)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'total_points', 'rank']
    
    def get_id(self, obj):
        return str(obj._id)

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'target_muscles']
    
    def get_id(self, obj):
        return str(obj._id)
