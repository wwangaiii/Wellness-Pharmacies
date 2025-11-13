from django.db import models

class Medicine(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField()
     price = models.DecimalField(max_digits=10, decimal_places=2)
     stock = models.IntegerField()
     expiry_date = models.DateField()

     def __str__(self):
         return self.name
     
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Order(models.Model):
     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
     order_date = models.DateTimeField(auto_now_add=True)
     total_amount = models.DecimalField(max_digits=10, decimal_places=2)

     def __str__(self):
         return f"Order {self.id} by {self.customer}" 


class OrderItem(models.Model):
     order = models.ForeignKey(Order, on_delete=models.CASCADE)
     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
     quantity = models.IntegerField()
     price = models.DecimalField(max_digits=10, decimal_places=2)

     def __str__(self):
         return f"{self.quantity} of {self.medicine.name} in Order {self.order.id}"   

     def save(self, *args, **kwargs):    
        self.price = self.medicine.price * self.quantity
        super().save(*args, **kwargs)
