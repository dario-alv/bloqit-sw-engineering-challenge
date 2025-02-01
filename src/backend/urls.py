from django.urls import path, include

from backend.views.user import UserRegistrationView, LoginView, LogoutView

urlpatterns = [

    path('user/', include([
        path('registration/', UserRegistrationView.as_view(), name='registration'),
        path('login/',  LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
    ]))

]
