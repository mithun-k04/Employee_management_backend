from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')

urlpatterns = [
    path('', include(router.urls)),
    path("hrlogin/", LoginHrclass.as_view(), name="hrlogin"),
]
