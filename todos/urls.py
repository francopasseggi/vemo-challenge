from django.urls import include, path
from rest_framework import routers

from todos.views import TodoModelViewSet

router = routers.DefaultRouter()
router.register(r"todos", TodoModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
