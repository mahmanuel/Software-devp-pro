from django.urls import path
from . import views

# URLConfig
urlpatterns = [
    path("hello/", views.say_hello),
    path("api/issues/", views.issue_list, name="issue_list"),
]

from django.urls import path
from .views import LoginView, LogoutView, UserProfileView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"profiles", ProfileViewSet)
router.register(r"discussion_forums", DiscussionForumViewSet)
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"research_materials", ResearchMaterialViewSet)
router.register(r"group_projects", GroupProjectViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"feedback", FeedbackViewSet)
router.register(r"events", EventViewSet)
router.register(r"mentorships", MentorshipViewSet)
router.register(r"activities", ActivityViewSet)
router.register(r"external_integrations", ExternalIntegrationViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
