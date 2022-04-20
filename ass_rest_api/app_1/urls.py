from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Your URLs...
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegister.as_view() , name='register'),
    path('home/' , HomeUser.as_view() , name= 'home'),
    path('update/<int:pk>/' , HomeEdit.as_view() , name= 'edit_delete'),
    


   
]