from django.contrib import admin

from .models import Classes, Courses, News, Messages

admin.site.register(Courses)
admin.site.register(Classes)
admin.site.register(News)
admin.site.register(Messages)