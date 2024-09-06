from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Date, Calendar

admin.site.register(User)
admin.site.register(Date)
admin.site.register(Calendar)