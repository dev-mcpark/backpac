from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.utils.deconstruct import deconstructible

from django.utils.translation import ugettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+\Z'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0


class Member(AbstractUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )

    username_validator = UsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=20,
        help_text=_('Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
    )

    nickname = models.CharField(max_length=30, validators=[])
    phone = models.CharField(max_length=20, validators=[])
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), blank=True, null=True)

    USERNAME_FIELD = 'email'
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')


class Order(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=12, unique=True)
    product = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now_add=True)
