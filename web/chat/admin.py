from django.contrib import admin
from .models import Chat, Message, UserReview
from user.models import User

# admin.site.register(User)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(UserReview)