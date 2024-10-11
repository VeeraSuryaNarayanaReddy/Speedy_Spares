from django.apps import AppConfig
import importlib

class Speedyapp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'speedyapp1'


    def ready(self) -> None:
        from django.contrib.auth.models import User
        def get_cart_count(user):
            from .models import CartItem
            return CartItem.objects.filter(cart__is_paid=False,cart__user=user).count()
        
        User.add_to_class('get_cart_count',get_cart_count)