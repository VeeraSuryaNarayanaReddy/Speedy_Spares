from django.db import models
from accounts.models import *
from django.db.models import Model,Sum,F
# Create your models here.
class Brand(BaseModel):
    brand_name = models.CharField(max_length=100)
    brand_image = models.ImageField(upload_to='static/imges/brands')
    def __str__(self) -> str:
        return self.brand_name

class Brand_models(BaseModel):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    model_image = models.ImageField(upload_to='static/imges/models')

    def __str__(self) -> str:
        return self.model_name

class Spares(BaseModel):
    model = models.ForeignKey(Brand_models,on_delete=models.CASCADE)
    spare_name=models.CharField(max_length=100)
    spare_image=models.ImageField(upload_to='static/imges/spares')
    spare_price = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    rating = models.IntegerField(default=4)
    def __str__(self) -> str:
        return self.spare_name
    

class Cart(BaseModel):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name='carts')
    is_paid=models.BooleanField(default=False)

    def get_cart_total(self):
        total_price = CartItem.objects.filter(cart=self).aggregate(total_price=Sum(F('quantity') * F('products__spare_price')))['total_price']
        return total_price if total_price else 0

class CartItem(BaseModel):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items')
    products=models.ForeignKey(Spares,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Add total_price field

    def save(self, *args, **kwargs):
        # Calculate total price before saving
        self.total_price = self.products.spare_price * self.quantity
        super().save(*args, **kwargs)
    