from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from sis_credito.views import CreditFormViewSet

router = routers.DefaultRouter()
router.register(r'sis_credito', CreditFormViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]