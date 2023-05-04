from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    cm_id = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=255, null=True)
    born_date = models.DateField(null=True)
    joined_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name
        
class Product(models.Model):
    pr_id = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    describe = models.CharField(max_length=255, null=True)
    origin = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='img_product/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    od_id = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.id)
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=False, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product.name

    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)