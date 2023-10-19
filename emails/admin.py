from django.contrib import admin
from .models import List, Subscriber, Email


admin.site.register(List)
admin.site.register(Subscriber)
admin.site.register(Email)