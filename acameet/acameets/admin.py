from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Profile)
admin.site.register(DiscussionForum)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ResearchMaterial)
admin.site.register(GroupProject)
admin.site.register(Task)
admin.site.register(Feedback)
admin.site.register(Event)
admin.site.register(Mentorship)
