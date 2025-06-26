from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')

<<<<<<< HEAD

=======
>>>>>>> 62506c085f34622a671ae78a64637786ee561545
urlpatterns = [
    path('', include(router.urls)),
    path("hrlogin/", LoginHrclass.as_view(), name="hrlogin"),
    path("addemployee/", AddEmployee.as_view(), name="addemployee"),
<<<<<<< HEAD
    path("leaverecords/<int:id>", GetLeaveById.as_view()),
    path('updateleave/<int:id>/', LeaveUpdate.as_view()),
    path('employeelogin/', EmployeeValidation.as_view(),),
    path("leaverecord/<str:email>", GetLeaveByEmail.as_view()),
=======
>>>>>>> 62506c085f34622a671ae78a64637786ee561545
]
