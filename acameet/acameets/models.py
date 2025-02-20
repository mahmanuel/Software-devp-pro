from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# user Profile extension
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("mentor", "Mentor"),
        ("admin", "Admin"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="student")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile/", blank=True, null=True)
    expertise = models.CharField(max_length=255, blank=True, null=True)
    is_mentor = models.BooleanField(default=False)
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username


# Discussion Forum
class DiscussionForum(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    forum = models.ForeignKey(
        DiscussionForum, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"Post by {self.created_by.username} in {self.forum.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.Textfield()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.created_by.username} on {self.post.id}"


# Research Material
class ResearchMaterial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to="research_materials/")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


# Collaboration Tools
class GroupProject(models.Model):
    title = models.CharField(max_lengths=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="group_projects")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    project = models.ForeignKey(
        GroupProject, on_delete=models.CASCADE, related_name="tasks"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Completed", "Completed")],
        default="Pending",
    )
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="feedback_received"
    )
    given_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="feedback_given"
    )
    comments = models.TextField()
    rating = models.IntegerField(default=1)  # 1-5 rating scale
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.student.username} by {self.given_by.username}"


# Event Management
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User, related_name="events_attended", blank=True)

    def __str__(self):
        return self.title


# Mentorship Program
class Mentorship(models.Model):
    mentor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mentorships_as_mentor"
    )
    mentee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mentorships_as_mentee"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.Charfield(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Active", "Active"),
            ("Completed", "Completed"),
        ],
        default="Pending",
    )

    def __str__(self):
        return f"{self.mentee.username} mentored by {self.mentor.username}"


# Activity Feed
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Activity by {self.user.username}"


# Integration with External Platforms
class ExternalIntegration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(
        max_length=50,
        choices=[
            ("LinkedIn", "LinkedIn"),
            ("ResearchGate", "ResearchGate"),
            ("GitHub", "GitHub"),
        ],
    )
    profile_link = models.URLField()

    def __str__(self):
        return f"{self.user.username} - {self.platform}"
