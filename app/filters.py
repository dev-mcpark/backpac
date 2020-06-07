import django_filters

from app.models import Member


class UserFilter(django_filters.rest_framework.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Member
        fields = ['username', 'email']
