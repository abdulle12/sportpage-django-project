from django.contrib import admin

# Register your models here.
from .models import Homepage
from .models import Homepage1
from .models import Homepage2
from .models import Homepage3

admin.site.register(Homepage)
admin.site.register(Homepage1)
admin.site.register(Homepage2)
admin.site.register(Homepage3)

