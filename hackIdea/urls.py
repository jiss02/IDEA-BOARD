from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from ideas.views import IdeaViewSet

router = routers.DefaultRouter()
router.register('ideas', IdeaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
