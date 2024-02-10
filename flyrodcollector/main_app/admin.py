from django.contrib import admin
from .models import Flyrod
from .models import Flyreel
from .models import Trip


# Register your models here.

admin.site.register(Flyrod)
admin.site.register(Flyreel)
admin.site.register(Trip)