from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tournament(models.Model):
    name = models.CharField(null=False, max_length=100)


class Groupe(models.Model):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    GROUPE_NAMES = {
        A : A,
        B : B,
        C : C,
        D : D,
        E : E,
        F : F,
    }
    name = models.CharField(null=False, 
                            max_length=1,
                            choices=GROUPE_NAMES)
    tournament = models.ForeignKey(Tournament, 
                                   null=True, 
                                   on_delete=models.DO_NOTHING)


class Team(models.Model):
    name = models.CharField(max_length=100)
    flag_id = models.IntegerField(null=True)
    groupe = models.ForeignKey(Groupe, null=True, on_delete=models.DO_NOTHING)


class Match(models.Model):
    PRELIMENARY='PRELIMENARY'
    FINALS_8   = 'FINALS_8'
    FINALS_4   = 'FINALS_4' 
    FINALS_2   = 'FINALS_2'
    FINAL      = 'FINAL'
    MATCH_TYPES = {
        PRELIMENARY:'prelimenary', 
        FINALS_8   : 'finals_8',
        FINALS_4   : 'finals_4', 
        FINALS_2   : 'finals_2', 
        FINAL      : 'final'
    }
    date = models.DateField()
    home_team = models.ForeignKey(Team, related_name="home_team", on_delete=models.DO_NOTHING)
    home_goals = models.IntegerField(null=True, default=None)
    away_team = models.ForeignKey(Team, related_name="away_team", on_delete=models.DO_NOTHING)
    away_goals = models.IntegerField(null=True, default=None)
    # 'prelimenary', 'finals_8', 'finals_4', 'finals_2', 'final'
    match_type = models.CharField(
        null=True, 
        max_length=11,
        choices=MATCH_TYPES) 
    tournament = models.ForeignKey(Tournament, 
                                   null=True, 
                                   on_delete=models.DO_NOTHING)


class Tipp(models.Model):
    match = models.ForeignKey(Match,on_delete=models.DO_NOTHING)
    home_goals = models.IntegerField(null=True)
    away_goals = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    
