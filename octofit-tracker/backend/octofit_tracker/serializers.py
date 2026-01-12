from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team', 'team_id']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'type', 'duration', 'date']

class WorkoutSerializer(serializers.ModelSerializer):
    suggested_for = UserSerializer(many=True, read_only=True)
    suggested_for_ids = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='suggested_for', many=True, write_only=True, required=False)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for', 'suggested_for_ids']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'score']
