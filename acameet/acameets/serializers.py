from rest_framework import serializers
from django.contrib.auth.models import User
from acameets.models import (
    Activity,
    Comment,
    DiscussionForum,
    Event,
    ExternalIntegration,
    Feedback,
    GroupProject,
    Mentorship,
    Post,
    ResearchMaterial,
    Task,
)
from .models import *


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DiscussionForum
        fields = "__all__"


# discussion Forum
class DiscussionForumSerializer(serializers.ModelSerializers):
    class Meta:
        model = DiscussionForum
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


# Research Material
class ResearchMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchMaterial
        fields = ""


# Collaboration
class GroupProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupProject
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


# Peer Feedback
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


# Events
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


# Mentorship
class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = "__all__"


# Activity Feed
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


# External Integrations
class ExternalIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalIntegration
        fields = "__all__"
