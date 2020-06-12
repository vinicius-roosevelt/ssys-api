
from django.contrib import admin
from django.urls import path, include
from core.views import EmployeeViewSet,ReportViewSet
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.SimpleRouter()
router.register('employees', EmployeeViewSet)
router.register('reports/employees', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/',views.obtain_auth_token, name="api-token-auth"),
]
