from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from app.models import Order

User = get_user_model()


class MemberAdmin(UserAdmin):
    model = User
    list_display = [
        'email', 'username', 'nickname', 'phone', 'gender', 'is_active', 'date_joined', 'last_login',
        'is_staff', 'is_superuser'
    ]
    list_filter = (
        'date_joined',
    )
    search_fields = ('email', 'username')


admin.site.register(User, MemberAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'product', 'payment_date']
    search_fields = ('order_number',)
    raw_id_fields = ['user']


admin.site.register(Order, OrderAdmin)
