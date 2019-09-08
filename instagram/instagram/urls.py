from django.contrib import admin
from django.urls import path, include
# include로 연결

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insta.urls')),
]
