from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, LoginLog, TeacherStudent

class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    list_display = ('username', 'email', 'user_type', 'is_active', 'is_staff')
    list_filter = ('user_type', 'is_active', 'is_staff')  # Filters for the admin list view
    search_fields = ('username', 'email')  # Fields that can be searched in the admin
    ordering = ('username',)
    
    # Fields to be displayed in the detail view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type', 'is_active', 'is_staff')}
        ),
    )


# Register the custom UserAdmin with the User model
admin.site.register(User, UserAdmin)

admin.site.register(LoginLog)
admin.site.register(TeacherStudent)