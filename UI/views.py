from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .models import Tipp
from .serializers import TippSerializer
from .models import Match
from .serializers import MatchSerializer
from .models import Team
from .serializers import TeamSerializer
from .models import Groupe
from .serializers import GroupeSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TippViewSet(viewsets.ModelViewSet):
    queryset = Tipp.objects.all()
    serializer_class = TippSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    # permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get_queryset(self):
        return self.queryset
    
    @csrf_exempt
    def retrieve(self, request, pk=None):
        m = get_object_or_404(self.queryset, pk = pk)
        serializer = MatchSerializer(m)
        return Response(serializer.data)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    # permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get_queryset(self):
        return self.queryset
    

class GroupeViewSet(viewsets.ModelViewSet):
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer
    # permission_classes = [IsAuthenticated]

    @csrf_exempt
    def get_queryset(self):
        return self.queryset
    

from django.shortcuts import render

def index(request):
    return render(request, 'UI/index.html')

def login(request):
    return render(request, 'UI/login.html')

def register(request):
    return render(request, 'UI/register.html')

@csrf_exempt
def get_matches(request):
    """
    Liste alle Matches auf.
    """
    if request.method == 'GET':
        matches = Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    

@csrf_exempt
def get_match(request):
    """
    Liste alle Matches auf.
    """
    if request.method == 'GET':
        match_id = int(request.GET.get('id'))
        matches = Match.objects.all()
        serializer = MatchSerializer(matches.filter(id=match_id), many=True)
        return JsonResponse(data=serializer.data[0], safe=False)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer