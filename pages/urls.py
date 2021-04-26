from django.urls import path

from .views import HomePageView, UserList, UserDetail, UserListUpdate, UserListDelete, UserListView


urlpatterns = [
    path('users/', UserListView.as_view(), name='users'),
    path('<int:pk>/edit/', UserListUpdate.as_view(), name='user_edit'),
    path('<int:pk>/delete/', UserListDelete.as_view(), name='user_delete'), # new
    path('users/<int:pk>/', UserDetail.as_view()),
    path('', HomePageView.as_view(), name='home'),
]