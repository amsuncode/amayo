from django.contrib import admin

# Register your models here.
from .models import Course, Paper #, Question

admin.site.register(Course)
# admin.site.register(Paper)
# admin.site.register(Question)