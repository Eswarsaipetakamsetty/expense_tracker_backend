from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('expenses', ExpenseView, basename='expenses')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('signup/', RegisterView.as_view(), name='user_signup'),
    path('', include(router.urls))
]
