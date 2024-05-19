from django.contrib import admin
from .models import MyUser, CV, CVView

admin.site.register(MyUser)
admin.site.register(CV)
admin.site.register(CVView)


