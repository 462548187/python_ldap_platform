from django.contrib import admin

# Register your models here.
from accounts.models import User, UserLoginInfo


class UserInfoAdmin(admin.ModelAdmin):
    search_fields = ('username',)


admin.site.register(User, UserInfoAdmin)
admin.site.register(UserLoginInfo)
