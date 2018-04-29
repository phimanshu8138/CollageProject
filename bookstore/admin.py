from django.contrib import admin

from .models import Regis_db
from .models import contact_db
from .models import donate_db

admin.site.register(Regis_db)
admin.site.register(donate_db)
admin.site.register(contact_db)
