from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from ideas.views import IdeaViewSet
# from join.views import JoinViewSet

router = routers.DefaultRouter()
# router.register('ideas', IdeaViewSet)
# router.register('joins', JoinViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ideas/', include('ideas.urls')),
]
