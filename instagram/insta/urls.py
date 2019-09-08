from django.urls import path
from . import views
# 내가 있는 파일에서 import 해옴

urlpatterns = [
    path('', views.main, name="main"),
]
