from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Issue

# Create your views here. request handler
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.role == "admin":
            return Response({"message": "Welcome, Admin!"})
        elif request.user.role == "mentor":
            return Response({"message": "Welcome, Mentor!"})
        return Response({"message": "Welcome, Student!"})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "role"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return {"token": token.key, "user": UserSerializer(user).data}
        raise serializers.ValidationError("Invalid credentials")


from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, UserSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


def say_hello(request):
    return render(request, "hello.html", {"name": "Mah"})


def issue_list(request):
    issues = Issue.objects.all().values("id", "title", "description")
    return JsonResponse(list(issues), safe=False)


from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


# User & Profile
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


# Discussion Forum
class DiscussionForumViewSet(viewsets.ModelViewSet):
    queryset = DiscussionForum.objects.all()
    serializer_class = DiscussionForumSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


# Research Material
class ResearchMaterialViewSet(viewsets.ModelViewSet):
    queryset = ResearchMaterial.objects.all()
    serializer_class = ResearchMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]


# Collaboration
class GroupProjectViewSet(viewsets.ModelViewSet):
    queryset = GroupProject.objects.all()
    serializer_class = GroupProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


# Peer Feedback
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]


# Events
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


# Mentorship
class MentorshipViewSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer
    permission_classes = [permissions.IsAuthenticated]


# Activity Feed
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]


# External Integration
class ExternalIntegrationViewSet(viewsets.ModelViewSet):
    queryset = ExternalIntegration.objects.all()
    serializer_class = ExternalIntegrationSerializer
    permission_classes = [permissions.IsAuthenticated]
