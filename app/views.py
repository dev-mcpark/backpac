from django.shortcuts import render

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from app.filters import UserFilter
from app.helper import make_unique_order_number
from app.models import Member, Order
from app.serializers import UserSerializer, OrderSerializer


class MyPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class UserRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Member.objects.all()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Member.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    pagination_class = MyPagination


class UserOrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        user = get_object_or_404(Member, pk=self.kwargs.get('pk'))
        queryset = queryset.filter(user=user)
        return queryset


class OrderCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            order_number=make_unique_order_number()
        )
