from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')


urlpatterns = [
    path('', include(router.urls)),
    path("hrlogin/", LoginHrclass.as_view(), name="hrlogin"),
    path("addemployee/", AddEmployee.as_view(), name="addemployee"),
    path("leaverecords/<int:id>", GetLeaveById.as_view()),
    path('updateleave/<int:id>/', LeaveUpdate.as_view()),
    path('employeelogin/', EmployeeValidation.as_view(),),
    path("leaverecord/<str:email>", GetLeaveByEmail.as_view()),
]
