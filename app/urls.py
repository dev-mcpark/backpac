from django.urls import path

from app.views import UserRetrieveView, UserListView, UserOrderListView

app_name = 'app'
urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserRetrieveView.as_view(), name='user_detail'),
    path('users/<int:pk>/orders/', UserOrderListView.as_view(), name='order_list')
]
