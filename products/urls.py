from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, UserAPIView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('', include(router.urls)),
]
