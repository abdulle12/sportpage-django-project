from django.contrib import admin

# Register your models here.
from .models import Homepage
from .models import Homepage1
from .models import Homepage2
from .models import Homepage3
from .models import Newspage1
from .models import Newspage2
from .models import Newspage3
from .models import Newspage4

#homepage models
admin.site.register(Homepage)
admin.site.register(Homepage1)
admin.site.register(Homepage2)
admin.site.register(Homepage3)

#newspage models
admin.site.register(Newspage1)
admin.site.register(Newspage2)
admin.site.register(Newspage3)
admin.site.register(Newspage4)


