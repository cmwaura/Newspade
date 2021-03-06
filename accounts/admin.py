from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

user = get_user_model()

# Register your models here.
class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

class UserProfileAdmin(UserAdmin):
	inlines =(UserProfileInline,)

admin.site.unregister(user)
admin.site.register(get_user_model(), UserProfileAdmin)