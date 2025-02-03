from django.urls import path, include

from backend.views.bloq import CreateBloqView, ListBloqView, RetrieveBloqView, EditDeleteBloqView
from backend.views.locker import CreateLockerView, ListLockerView, UpdateLockerView, DeleteLockerView 
from backend.views.rent import CreateRentView, ListRentView, UpdateRentView 
from backend.views.user import UserRegistrationView, LoginView, LogoutView


urlpatterns = [

    path('user/', include([
        path('registration/', UserRegistrationView.as_view(), name='registration'),
        path('login/',  LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
    ])),

    path('bloq/', include([
        path('create/', CreateBloqView.as_view(), name='bloq_create'), 
        path('list/', ListBloqView.as_view(), name='bloq_list'),
        path('<str:id>/get/', RetrieveBloqView.as_view(), name='bloq_retrieve'),
        path('<str:id>/', EditDeleteBloqView.as_view(), name='bloq_edit_delete'),
    ])),

    path('locker/', include([
        path('create/', CreateLockerView.as_view(), name='locker_create'),
        path('list/', ListLockerView.as_view(), name='locker_list'),
        path('<str:id>/', UpdateLockerView.as_view(), name='locker_retrieve_update'),
        path('<str:id>/delete/', DeleteLockerView.as_view(), name='locker_delete'),
    ])),
    
    path('rent/', include([
        path('create/', CreateRentView.as_view(), name='rent_create'),
        path('list/', ListRentView.as_view(), name='rent_list'),
        path('<str:id>/', UpdateRentView.as_view(), name='rent_retrieve_update_delete'),
    ]))
]
