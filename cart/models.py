from django.db import models
from products.models import Product
import uuid # Required for unique cart instances 
from django.contrib.auth.models import User
# Create your models here.

class CartItem(models.Model):
    """ eeew """
    pass
    m = models.ForeignKey(Product,  on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #cart = models.ForeignKey('testCart', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    order_id = models.ForeignKey('TestCart', on_delete=models.SET_NULL, null=True)
    
    def getPrice(self):
        return self.m.price
    
    def getLineTotal(self):
        return round(self.m.price * self.quantity,2)

    def increaseQuantity(self):
        self.quantity += 1
        self.save()
    
    def decreaseQuantity(self):
        self.quantity -=1
        if self.quantity < 1:
            self.quantity = 1
        self.save()

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.m} x  [{self.quantity}]  For: {self.order_id}'

    
    


class TestCart(models.Model):
    """Model representing a specific instance of a cart (i.e. that can be tracked in warehouse)."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular product across whole system')
    itemsInCart = models.ManyToManyField(CartItem)
    cartOwner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total = f'0.00'

    #productLine = models.CharField(max_length=200)
    #theStuff = models.ManyToManyFi(otherCart, on_delete=models.SET_NULL, null=True)
    #product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True) 
    #productList = models.ManyToManyField(Product)
    #productLine = models.CharField(max_length=200)
    next_ship = models.DateField(null=True, blank=True)
    #category = models.ManyToManyField(Category, help_text='Select a category for this product')


    CART_STATUS = (
        ('b', 'Browsing'),
        ('p', 'Paid Order'),
        ('s', 'Shipped'),
        ('c', 'Cancelled'),
    )

    status = models.CharField(
        max_length=1,
        choices=CART_STATUS,
        blank=True,
        default='t',
        help_text='Product availability',
    )

    class Meta:
        ordering = ['next_ship']

    def getTotal(self):
        """ get total for cart or order """
        total = 0
        for eachProduct in self.itemsInCart.all():
            total += eachProduct.getLineTotal()
        #return total
        return '${:,.2f}'.format(total)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.cartOwner}\'s Cart/Order id#  {self.id} total: {self.getTotal()}'


    def putInCart(self, product):
        """puts in cart, buy first making it a cart item from cart item class """
        user = self.cartOwner
        cartItem = CartItem(m=product,user_id=user)
        cartItem.save()
        self.itemsInCart.add(cartItem)
        self.save()












    