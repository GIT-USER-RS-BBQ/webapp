from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from .models import Tipp
from .models import Match
from .models import Team
from .models import Groupe

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TippSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipp
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Tipp-Enträge für die Vorrundenspiele anlegen
        for m in Match.objects.all():
            tipp = Tipp()
            tipp.user = user
            tipp.match = m
            tipp.home_goals = None
            tipp.away_goals = None
            Tipp.save(tipp)
            
        return user