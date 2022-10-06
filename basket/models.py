from django.db import models

# Create your models here.
class Basket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=30, null=False)
    order_date = models.DateTimeField(auto_now_add=True,)
    completedOrder = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_basket_items(self):
        basketitems = self.basketitems_set.all()
        total = sum([item.quantity for item in basketitems])
        return total

    @property
    def get_basket_total(self):
        basketitems = self.basketitems_set.all()
        total = sum([item.add_total for item in basketitems])
        return total